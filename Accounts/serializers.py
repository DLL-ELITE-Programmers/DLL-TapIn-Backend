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
      "department",
      "department_info",
      "is_superuser",
      "password"
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
      email=validated_data.get("email", ""),
      department=validated_data.get("department", ""),
      is_superuser=validated_data.get("is_superuser", False),
    )
    user.set_password(validated_data["password"]) 
    user.save()
    return user

  def get_department_info(self, obj):
    if obj.department:
      return DepartmentSerializer(obj.department).data
    return "Sana ako na lang"
