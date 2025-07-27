from rest_framework import serializers

from Events.models import Event, Participant


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ["event_id"]


class ParticipantSerializer(serializers.ModelSerializer):
    event_info = serializers.SerializerMethodField()
    participant_info = serializers.SerializerMethodField()

    class Meta:
        model = Participant
        fields = ["event_info", "participant_info"]

    def get_event_info(self, obj):
        return Event.objects.get(obj)

    def get_participant_info(self, obj):
        return Participant.objects.get(obj)
