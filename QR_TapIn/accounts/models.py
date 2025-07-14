from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class Department(models.Model):
    department_id = models.CharField(max_length=10, default="BSIT")
    department_name = models.CharField(max_length=100, default="Bachelor of Science in Information Technology")

    def __str__(self):
        return f"{self.department_id}"

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    middle_name = models.CharField(
        max_length=25, null=True, blank=True, default="", editable=True
    )
    sex = models.IntegerField(
        choices=[(0, "Female"), (1, "Male"), (2, "Others")], default=2
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="user", default="", null=True, blank=True)