from django.db import models

from BaseAuth.models import CoreModel

# Create your models here.


class Department(CoreModel):
  order = "department_id"

  department_id = models.CharField(max_length=10, default="BS")
  department_name = models.CharField(
    max_length=100, default="Bachelor of Science in "
  )

  def __str__(self):
    return f"{self.department_id}"


class Organization(CoreModel):
  order = "organization_name"

  organization_id = models.CharField(max_length=100, default="")
  organization_name = models.CharField(max_length=100, default="", blank=False)
  department = models.ManyToManyField(Department)

  def __str__(self):
    return f"{self.organization_id}"
