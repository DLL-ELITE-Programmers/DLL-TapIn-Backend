from Accounts.models import Student, User
from Organizations.serializers import DepartmentSerializer
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    student_details = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ["student_id", "student_details", "verified"]

    def get_student_details(self, obj):
        return UserSerializer(obj.student_info).data


class UserSerializer(serializers.ModelSerializer):
    department_info = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "middle_name",
            "last_name",
            "sex",
            "email",
            "department_info",
        ]

    def get_department_info(self, obj):
        if obj.department:
            return DepartmentSerializer(obj.department).data
        return "Sana ako na lang"
