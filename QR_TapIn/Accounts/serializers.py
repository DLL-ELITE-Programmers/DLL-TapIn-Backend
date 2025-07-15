from rest_framework import serializers
from .models import Department, Student, User

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    student_details = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = "__all__"

    def get_student_details(self, obj):
        user = User.objects.get(id__exact=obj.id)
        return UserSerializer(user).data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"