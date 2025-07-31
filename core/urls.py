from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter

from core.views import _404, main
from core.viewsets.updates import UpdatesAPI
from QR_TapIn.urls import api

urlpatterns = [
    path("", main),
    path(f"{api}updates/", UpdatesAPI.as_view()),
    re_path(r"^.*$", _404),
]
