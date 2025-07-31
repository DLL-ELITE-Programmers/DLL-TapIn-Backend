import pandas as pd
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Accounts.models import User
from BaseAuth.paginator import TenRowPaginator
from BaseAuth.views import BaseAuthModelViewset
from Events.models import Event, Participant
from Events.serializers import ParticipantSerializer


class ParticipantViewset(BaseAuthModelViewset):
    permission_classes = [AllowAny]
    queryset = Participant.objects.filter()
    serializer_class = ParticipantSerializer
    pagination_class = TenRowPaginator

    def list(self, req, *args, **kwargs):
        try:
            query = self.request.query_params

            if query.get("event"):
                self.queryset = Participant.objects.filter(
                    event__exact=query.get("event")
                )
            if query.get("user"):
                userID = User.objects.get(username=query.get("user").upper()).id
                self.queryset = Participant.objects.filter(participant__exact=userID)

            page = self.paginate_queryset(self.queryset)

            if page:
                data = self.serializer_class(page, many=True)
                data = self.get_paginated_response(data.data)
                return data

            data = self.serializer_class(self.queryset.all(), many=True)

            return Response({"total": self.queryset.count(), "data": data.data})

        except Exception as e:
            return Response({"error": str(e)})

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            event = Event.objects.get(event_id=data["event"]).event_id
            participant = User.objects.get(username__iexact=data["participant"]).id

            existing = Participant.objects.filter(
                event=event, participant=participant
            ).exists()

            if existing:
                return Response({"error": "The student is already registered"})

            serialize = self.serializer_class(
                data={"event": event, "participant": participant}, partial=True
            )
            if serialize.is_valid():
                serialize.save()
                return Response({"message": "Student is now participating"})
            return Response({"error": self.extract_error_handler(serialize.errors)})
        except Exception as e:
            return Response({"error": str(e)})

    @action(
        detail=False, url_path="export", methods=["GET"], permission_classes=[AllowAny]
    )
    def record(self, request):
        query = self.request.query_params

        try:
            if query.get("event"):
                event_id = query.get("event")
                participant = Participant.objects.filter(event=event_id)
                if not participant:
                    raise Exception("Invalid event")

                data = self.serializer_class(participant.all(), many=True).data
                info = [
                    item["participant_info"]
                    for item in data
                    if "participant_info" in item
                ]

                dataframe = pd.DataFrame(info)
                response = HttpResponse(
                    content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                response["Content-Disposition"] = (
                    f'attachment; filename="participants-{event_id}.xlsx"'
                )
                dataframe.to_excel(response, index=False)
                return response
        except Exception as e:
            return Response({"error": str(e)})
        return Response({"error": "Event is invalid"})
