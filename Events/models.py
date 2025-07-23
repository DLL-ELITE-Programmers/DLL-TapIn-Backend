from django.db import models
from django.utils.timezone import datetime

from Accounts.models import User
from Organizations.models import Organization

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=100, default="", null=False)
    event_description = models.TextField()
    event_venue = models.CharField(max_length=100, default="", null=False)
    handler = models.ManyToManyField(Organization)
    time_in = models.DateTimeField(default=datetime.now())
    time_out = models.DateTimeField(default=datetime.now())


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    time_in = models.DateField(auto_now_add=True)
    time_in = models.DateField(auto_now=True)
