from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from BaseAuth.views import BaseAuthModelViewset
from Events.models import Event
from Events.serializers import EventSerializers
from Events.views import generate_id
from Organizations.models import Organization


class EventViewset(BaseAuthModelViewset):
    permission_classes = [AllowAny]
    queryset = Event.objects.filter()
    serializer_class = EventSerializers

    def list(self, req, *args, **kwargs):
        try:
            query = self.request.query_params

            data = self.serializer_class(self.queryset.all(), many=True)
            if query.get("key"):
                self.queryset = Event.objects.get(event_id=query.get("key"))
                data = self.serializer_class(self.queryset)
            return Response(data.data)
        except Exception as e:
            return Response({
                "error": "Event code not found"
            })
        
    def create(self, request, *args, **kwargs):
        try:
            data = request.data.copy()

            print(data["organization"])

            orgs = data["organization"]
            organization = []
            for org in orgs:
                organization.append(int(Organization.objects.get(id=org).id))

            data["organization"] = organization

            data["event_id"] = generate_id(Event, "event_id")

            serialize = self.serializer_class(data=data, partial=True)
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
