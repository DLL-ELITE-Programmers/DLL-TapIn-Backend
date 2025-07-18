from django.urls import include, path
from Organizations.viewsets.department import DepartmentViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"department", DepartmentViewset, basename="department")

urlpatterns = [path("", include(router.urls))]
