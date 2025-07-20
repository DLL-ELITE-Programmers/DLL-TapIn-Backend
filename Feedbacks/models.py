from django.db import models

from Accounts.models import User
from BaseAuth.models import CoreModel
from Events.models import Event

# Create your models here.


class Feedback(CoreModel):
    order = "id"

    user = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, default="", on_delete=models.CASCADE)
    mesasge = models.TextField()
