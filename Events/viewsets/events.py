from threading import ExceptHookArgs

from rest_framework import viewsets
from rest_framework.response import Response

from BaseAuth.views import BaseAuthModelViewset
from Events.models import Event
from Events.serializers import EventSerializers
from Organizations.models import Organization


class EventViewset(BaseAuthModelViewset):
    queryset = Event.objects.filter()
    serializer_class = EventSerializers

    def list(self, req, *args, **kwargs):
        query = self.request.query_params

        data = self.serializer_class(self.queryset.all(), many=True)
        return Response(data.data)

    def create(self, request, *args, **kwargs):
        try:
            data = request.data

            data["handler"] = Organization.objects.get(
                organization_id=data["organization_id"]
            ).id

            serialize = self.serializer_class(data, partial=True)
            if serialize.is_valid():
                serialize.save()
                return Response(
                    {
                        "message": "Event addes successfully",
                        "event_information": serialize.data,
                    }
                )

        except Exception as e:
            return Response({"error": self.extract_error_handler(e)})
