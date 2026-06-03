from rest_framework import serializers

from Accounts.models import User
from Departments.serializers import DepartmentSerializer


class UserSerializer(serializers.ModelSerializer):
    department_id = serializers.SerializerMethodField()
    department_name = serializers.SerializerMethodField()
    sex_display = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "middle_name",
            "last_name",
            "sex_display",
            "email",
            "department_id",
            "department_name",
            "is_superuser",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            first_name=validated_data.get("first_name", ""),
            middle_name=validated_data.get("middle_name", ""),
            last_name=validated_data.get("last_name", ""),
            sex=validated_data.get("sex", 0),
            year=validated_data.get("year", 1),
            section=validated_data.get("section", "A").upper(),
            email=validated_data.get("email", ""),
            department=validated_data.get("department", ""),
            is_superuser=validated_data.get("is_superuser", False),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def get_sex_display(self, obj):
        sex = ["Female", "Male", "Others"]
        return sex[obj.sex]

    def get_department_id(self, obj):
        if obj.department:
            return DepartmentSerializer(obj.department).data.get("department_id")
        return "Sana ako na lang"

    def get_department_name(self, obj):
        if obj.department:
            return DepartmentSerializer(obj.department).data.get("department_name")
        return "Sana ako na lang"
