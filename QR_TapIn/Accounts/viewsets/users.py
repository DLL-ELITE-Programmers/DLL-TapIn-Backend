from Accounts.models import User
from Accounts.serializers import UserSerializer
from BaseAuth.views import BaseAuthModelViewset


class UserViewset(BaseAuthModelViewset):
    queryset = User.objects.filter()
    serializer_class = UserSerializer

    def list(self, req, *args, **kwargs):
        query = self.request.query_params

        data = self.serializer_class(self.queryset.all(), many=True)
        return Response(data.data)
