from BaseAuth.views import BaseAuthModelViewset
from rest_framework.response import Response
from Accounts.serializers import StudentSerializer

class StudentViewSet(BaseAuthModelViewset):
    serializer_class = StudentSerializer

    def list(self, req, *args, **kwargs):
        query = self.request.query_params

        data = self.serializer_class(self.queryset, many=True)
        return Response(data.data)
