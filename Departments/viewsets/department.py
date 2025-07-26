from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from BaseAuth.views import BaseAuthModelViewset
from Departments.models import Department
from Departments.serializers import DepartmentSerializer


class DepartmentViewset(BaseAuthModelViewset):
    permission_classes = [AllowAny]
    queryset = Department.objects.filter()
    serializer_class = DepartmentSerializer

    def list(self, req, *args, **kwargs):
        query = self.request.query_params

        data = self.serializer_class(self.queryset, many=True)
        return Response(data.data)
