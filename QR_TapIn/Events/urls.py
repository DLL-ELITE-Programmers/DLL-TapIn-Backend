from django.urls import include, path
from Events.viewsets.events import EventViewset
from Events.viewsets.participants import ParticipantViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"events", EventViewset, basename="event")
router.register(r"participants", ParticipantViewset, basename="participant")

urlpatterns = [path("", include(router.urls))]
