from django.urls import include, path
from Organizations.viewsets.department import DepartmentViewset
from Organizations.viewsets.organization import OrganizationViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"department", DepartmentViewset, basename="department")
router.register(r"organization", OrganizationViewset, basename="organizations")

urlpatterns = [path("", include(router.urls))]
