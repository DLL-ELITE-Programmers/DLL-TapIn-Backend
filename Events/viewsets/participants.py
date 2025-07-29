from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Accounts.models import User
from BaseAuth.views import BaseAuthModelViewset
from Events.models import Event, Participant
from Events.serializers import ParticipantSerializer


class ParticipantViewset(BaseAuthModelViewset):
    permission_classes = [AllowAny]
    queryset = Participant.objects.filter()
    serializer_class = ParticipantSerializer

    def list(self, req, *args, **kwargs):
        try:
            query = self.request.query_params

            data = self.serializer_class(self.queryset.all(), many=True)
            return Response(data.data)

        except Exception as e:
            return Response({"error": str(e)})

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            event = Event.objects.get(event_id=data["event"]).event_id
            participant = User.objects.get(username__iexact=data["participant"]).id
            serialize = self.serializer_class(
                data={"event": event, "participant": participant}, partial=True
            )
            if serialize.is_valid():
                serialize.save()
                return Response({"message": "Student is now participating"})
            return Response({"error": self.extract_error_handler(serialize.errors)})
        except Exception as e:
            return Response({"error": str(e)})

        try:
            data = request.data
            serialize = self.serializer_class(data, partial=False)
            if serialize.is_valid():
                serialize.save()
                return Response({"message": "Participant registed"})
            return Response({"error": self.extract_error_handler(serialize.errors)})
        except Exception as e:
            return Response({"error": str(e)})
