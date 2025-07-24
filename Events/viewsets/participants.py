from rest_framework.response import Response

from BaseAuth.views import BaseAuthModelViewset
from Events.models import Participant
from Events.serializers import ParticipantSerializer


class ParticipantViewset(BaseAuthModelViewset):
    queryset = Participant.objects.filter()
    serializer_class = ParticipantSerializer

    def list(self, req, *args, **kwargs):
        query = self.request.query_params

        data = self.serializer_class(self.queryset.all(), many=True)
        return Response(data.data)
