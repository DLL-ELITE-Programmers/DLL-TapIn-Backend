from Events.models import Event
from Events.serializers import EventSerializers
from rest_framework import viewsets
from rest_framework.response import Response


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.filter()
    serializer_class = EventSerializers

    def list(self, req, *args, **kwargs):
        query = self.request.query_params

        data = self.serializer_class(self.queryset.all(), many=True)
        return Response(data.data)
