import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Department(models.Model):
    department_id = models.CharField(max_length=10, default="BSIT")
    department_name = models.CharField(
        max_length=100, default="Bachelor of Science in Information Technology"
    )

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
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="user",
        default="",
        null=True,
        blank=True,
    )

    def __str__(self):
        #     return self.id
        return f"{self.last_name}, {self.first_name}"


class Student(models.Model):
    student_id = models.CharField(
        max_length=25, default="012A-1234", primary_key=True, unique=True
    )
    student_info = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.student_id
