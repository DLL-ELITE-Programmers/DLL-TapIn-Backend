import secrets
import string

from django.shortcuts import render

# Create your views here.


def generate_unique_id(length=10):
    characters = string.ascii_lowercase + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))


def generate_id(model, field_name="event_id", length=10):
    while True:
        new_event_id = generate_unique_id()
        if not model.objects.filter(**{field_name: new_event_id}).exists():
            return new_event_id
