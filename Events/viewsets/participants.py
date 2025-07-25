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

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serialize = self.serializer_class(data, partial=False)
            if serialize.is_valid():
                serialize.save()
                return Response({"message": "Participant registed"})
            return Response({"error": self.extract_error_handler(serialize.errors)})
        except Exception as e:
            return Response({"error": str(e)})
