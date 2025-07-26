from django.db import models

from Accounts.models import Department, User
from BaseAuth.models import CoreModel

# Create your models here.


class Organization(CoreModel):
    order = "organization_name"

    organization_id = models.CharField(max_length=100, default="")
    organization_name = models.CharField(max_length=100, default="", blank=False)
    department = models.ManyToManyField(Department)

    officers = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.organization_id}"
