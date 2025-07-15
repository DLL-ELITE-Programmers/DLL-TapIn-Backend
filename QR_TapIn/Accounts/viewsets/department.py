from Accounts.serializers import DepartmentSerializer
from BaseAuth.views import BaseAuthModelViewset


class DepartmentViewset(BaseAuthModelViewset):
    serializer_class = DepartmentSerializer

    def list(self, req, *args, **kwargs):
        query = self.request.query_params

        data = self.serializer_class(self.queryset, many=True)
        return Response(data.data)
