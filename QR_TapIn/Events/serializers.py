from Events.models import Event
from rest_framework import serializers


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
