from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Accounts.models import User
from BaseAuth.views import BaseAuthModelViewset
from Events.models import Event, Participant
from Events.serializers import ParticipantSerializer
from BaseAuth.paginator import TenRowPaginator

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

            data = self.serializer_class(self.queryset.all(), many=True)
            # return Response(data.data)
            return Response(
                {
                    "total": self.queryset.count(),
                    "data": data.data
                }
            )


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
