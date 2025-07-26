from django.urls import include, path
from rest_framework.routers import SimpleRouter

from Accounts.viewsets.users import UserViewset

router = SimpleRouter()
router.register(r"users", UserViewset, basename="user")

urlpatterns = [path("", include(router.urls))]
