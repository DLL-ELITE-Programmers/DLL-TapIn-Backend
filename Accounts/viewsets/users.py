from django.contrib.auth import authenticate
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from Accounts.models import User
from Accounts.serializers import UserSerializer
from BaseAuth.views import BaseAuthModelViewset


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

    @action(
        detail=False, methods=["POST"], url_path="login", permission_classes=[AllowAny]
    )
    def login(self, request):
        data = request.data
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return Response({"error": "Please provide username and/or password"})

        user_data = authenticate(username=username, password=password)

        if not user_data:
            return Response({"error": "Invalid credentials"})

        refresh = RefreshToken.for_user(user_data)
        return Response(
            {
                "message": "User logged in",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "username": user_data.username,
                    "first_name": user_data.first_name,
                    "middle_name": user_data.middle_name,
                    "last_name": user_data.last_name,
                    "email": user_data.email,
                    "superuser": user_data.is_superuser,
                },
            }
        )

    @action(
        detail=False,
        methods=["POST"],
        url_path="register",
        permission_classes=[AllowAny],
    )
    def register(self, request):
        try:
            data = request.data

            data["username"] = data["student_id"]
            serializer = self.serializer_class(data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Account was registered"})
            return Response({"error": self.extract_error_handler(serializer.errors)})

        except Exception as e:
            return Response({"error": str(e)})
