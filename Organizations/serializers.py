from rest_framework import serializers

from Organizations.models import Department, Organization


class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Organization
    fields = "__all__"
