from Accounts.models import Student
from Accounts.serializers import StudentSerializer
from BaseAuth.views import BaseAuthModelViewset
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class StudentViewset(BaseAuthModelViewset):
    permission_classes = [AllowAny]
    queryset = Student.objects.filter()
    serializer_class = StudentSerializer

    def list(self, req, *args, **kwargs):
        query = self.request.query_params

        data = self.serializer_class(self.queryset.all(), many=True)
        return Response(data.data)
