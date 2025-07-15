import uuid

from BaseAuth.models import CoreModelDescending
from django.contrib.auth.models import AbstractUser
from django.db import models
from Organizations.models import Department

# Create your models here.


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


class Student(CoreModelDescending):
    order = "student_id"

    student_id = models.CharField(
        max_length=25, default="012A-1234", primary_key=True, unique=True
    )
    student_info = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.student_id
