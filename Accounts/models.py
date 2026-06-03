import re
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from Departments.models import Department

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
        related_name="users",
        null=True,
        blank=True,
    )
    year = models.IntegerField(default=1)
    section = models.CharField(max_length=1, default="A")
    officer = models.ForeignKey(
        Department, null=True, blank=True, on_delete=models.SET_NULL
    )

    verified = models.BooleanField(default=False)

    def __str__(self):
        #     return self.id
        return self.username

    def save(self, *args, **kwargs):
        self.username = self.username.upper()
        user_id_pattern = re.fullmatch(r"^(\d+[a-zA-Z]{1})-(\d+)$", self.username)
        if user_id_pattern or self.username == "K.GUIN":
            self.first_name = self.first_name.upper()
            if self.middle_name:
                self.middle_name = str(self.middle_name).upper()
            self.last_name = self.last_name.upper()
            self.email = self.email.lower()
            super().save(*args, **kwargs)
        return {"error", "Invalid user"}

    class Meta:
        ordering = ["-username"]
