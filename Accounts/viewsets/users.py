from Accounts.models import User
from Accounts.serializers import UserSerializer
from BaseAuth.views import BaseAuthModelViewset
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class UserViewset(BaseAuthModelViewset):
    permission_classes = [AllowAny]
    queryset = User.objects.filter()
    serializer_class = UserSerializer

    def list(self, req, *args, **kwargs):
        query = self.request.query_params

        if query.get("user"):
            self.queryset = User.objects.filter(username__iexact=query.get("user"))

        data = self.serializer_class(self.queryset.all(), many=True)
        return Response(data.data)

    @action(detail=False, methods=["POST"], url_path="register", permission_classes=[AllowAny])
    def register(self, request):
        try:
            data = request.data

            data["username"] = data["student_id"]
            serializer = self.serializer_class(data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Account was registered"
                })
            return Response({
                "error": self.extract_error_handler(serializer.errors)
            })
        
        except Exception as e:
            return Response({
                "error": str(e)
            })