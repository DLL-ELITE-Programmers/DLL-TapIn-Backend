from django.urls import include, path
from rest_framework.routers import SimpleRouter

from Accounts.tests import UserTest
from Accounts.viewsets.users import UserViewset

router = SimpleRouter()
router.register(r"users", UserViewset, basename="user")

urlpatterns = [
    #    path("usercase/", UserTest.as_view()),
    path("", include(router.urls))
]
