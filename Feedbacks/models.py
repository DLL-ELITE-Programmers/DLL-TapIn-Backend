from django.db import models

from Accounts.models import User
from BaseAuth.models import CoreModel, CoreModelDescending
from Events.models import Event

# Create your models here.


class Feedback(CoreModelDescending):
    # order = "time_added"

    user = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, default="", on_delete=models.CASCADE)
    title = models.CharField(max_length=250, default="")
    message = models.TextField()
    # time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
