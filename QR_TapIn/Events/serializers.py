from Events.models import Event, Participant
from rest_framework import serializers


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = "__all__"