from django.urls import include, path
from rest_framework.routers import SimpleRouter

from Departments.viewsets.department import DepartmentViewset

router = SimpleRouter()
router.register(r"department", DepartmentViewset, basename="department")

urlpatterns = [path("", include(router.urls))]
