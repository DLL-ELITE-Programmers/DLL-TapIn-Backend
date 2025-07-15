from django.urls import include, path
from Events.viewsets.events import EventViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"events", EventViewset, basename="event")

urlpatterns = [path("", include(router.urls))]
