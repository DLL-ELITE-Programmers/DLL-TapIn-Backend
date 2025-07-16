from django.urls import path, re_path
from BaseAuth.views import main, _404

urlpatterns = [
    path("", main),
    re_path(r'^.*/$', _404)
]