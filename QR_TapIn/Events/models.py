from datetime import datetime

from django.db import models
from Organizations.models import Organization

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=100, default="", null=False)
    event_description = models.TextField()
    event_venue = models.CharField(max_length=100, default="", null=False)
    handler = models.ManyToManyField(Organization)
    time_in = models.DateTimeField(default=datetime.now())
    time_out = models.DateTimeField(default=datetime.now())
