from Events.models import Event, Participant
from rest_framework import serializers


class EventSerializers(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = "__all__"

class ParticipantSerializer(serializers.ModelSerializer):
  event_info = serializers.SerializerMethodField()
  participant_info = serializers.SerializerMethodField()
  
  class Meta:
    model = Participant
    fields = [
      "event_info",
      "participant_info"
    ]
  
  def get_event_info(self, obj):
    return Event.objects.get(obj)
  
  def get_participant_info(self, obj):
    return Participant.objects.get(obj)
  