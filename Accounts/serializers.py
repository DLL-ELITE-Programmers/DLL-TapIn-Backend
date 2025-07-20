from rest_framework import serializers

from Accounts.models import User
from Organizations.serializers import DepartmentSerializer


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
            "is_superuser",
        ]

    def get_department_info(self, obj):
        if obj.department:
            return DepartmentSerializer(obj.department).data
        return "Sana ako na lang"
