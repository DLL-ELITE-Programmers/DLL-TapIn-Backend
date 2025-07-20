from django.urls import include, path
from rest_framework.routers import SimpleRouter

from Feedbacks.viewsets.feedback import FeedbackViewset

routes = SimpleRouter()
routes.register(r"feedback", FeedbackViewset, basename="feedback")

urlpatterns = [path("", include(routes.urls))]
