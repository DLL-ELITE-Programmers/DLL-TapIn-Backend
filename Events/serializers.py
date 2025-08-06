from rest_framework import serializers
from Accounts.models import User
from Events.models import Event, Participant
from Departments.serializers import DepartmentSerializer
from datetime import datetime


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ["event_id"]


class ParticipantSerializer(serializers.ModelSerializer):
    event_info = serializers.SerializerMethodField()
    participant_info = serializers.SerializerMethodField()
    time_in = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    time_out = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Participant
        fields = [
            "event",
            "event_info",
            "participant_info",
            "time_in",
            "time_out"
        ]

    def get_event_info(self, obj):
        event_ = Event.objects.get(event_id=obj.event)
        return {
            "event_code": event_.event_id,
            "event_name": event_.event_name,
            "event_description": event_.event_description,
            "event_venue": event_.event_venue
        }

    def get_participant_info(self, obj):
        sex = ["Female", "Male", "Others"]
        participant_ = User.objects.get(username=obj.participant)
        
        dept = {
            "department_id": "unknown",
            "department_name": "Sana ako na lang"
        }
        if participant_.department:
            dept = DepartmentSerializer(participant_.department).data
        
        year_level = (datetime.now().year - int(participant_.username[:3]) - 2000) + 1

        return {
            "student_id": participant_.username,
            "first_name": participant_.first_name,
            "middle_name": participant_.middle_name,
            "last_name": participant_.last_name,
            "sex": sex[participant_.sex],
            "department_id": dept.get("department_id"),
            "department_name": dept.get("department_name"),
            "year_level": year_level
        }

class ExportParticipantSerializer(serializers.ModelSerializer):
    participant = serializers.SerializerMethodField()
    
    class Meta:
        model = Participant
        fields = [
            "participant"
        ]
    
    def get_participant(self, obj):
        sex = ["Female", "Male", "Others"]
        participant_ = User.objects.get(username=obj.participant)
        
        dept = {
            "department_id": "unknown",
            "department_name": "Sana ako na lang"
        }
        if participant_.department:
            dept = DepartmentSerializer(participant_.department).data
        
        year_level = (datetime.now().year - int(participant_.username[:3]) - 2000) + 1

        return {
            "student_id": participant_.username,
            "first_name": participant_.first_name,
            "middle_name": participant_.middle_name,
            "last_name": participant_.last_name,
            "sex": sex[participant_.sex],
            "department_id": dept.get("department_id"),
            "department_name": dept.get("department_name"),
            "year_level": year_level
        }