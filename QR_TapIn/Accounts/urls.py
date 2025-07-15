from Accounts.viewsets.department import DepartmentViewset
from Accounts.viewsets.students import StudentViewset
from Accounts.viewsets.users import UserViewset
from django.urls import include, path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r"department", DepartmentViewset, basename="department")
router.register(r"student", StudentViewset, basename="student")
router.register(r"users", UserViewset, basename="user")

urlpatterns = [path("", include(router.urls))]
