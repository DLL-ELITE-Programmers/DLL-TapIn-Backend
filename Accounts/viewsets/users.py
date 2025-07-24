from django.contrib.auth import authenticate
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from Accounts.models import User
from Accounts.serializers import UserSerializer
from BaseAuth.views import BaseAuthModelViewset
from Organizations.models import Department
from QR_TapIn.email import sendEmail


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
        detail=False, methods=["GET"], url_path="self", permission_classes=[AllowAny]
    )
    def myself(self, request):
        query = self.request.query_params

        if query.get("user"):
            self.queryset = User.objects.get(username__iexact=query.get("user"))
            data = self.serializer_class(self.queryset)
            return Response(data.data)

        return Response({"error": "There is no user ID"})

    @action(
        detail=False,
        methods=["GET"],
        url_path="forgot-password",
        permission_classes=[AllowAny],
    )
    def forgotPassword(self, request):
        data = request.query_params
        sendEmail(data.get("email"), "I miss you")
        return Response(data)

    @action(
        detail=False, methods=["POST"], url_path="login", permission_classes=[AllowAny]
    )
    def login(self, request):
        data = request.data
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return Response({"error": "Please provide Student ID and/or Password"})

        username = username.upper()

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

            if not data["student_id"] or not data["password"]:
                return Response({"error": "Please provide your information"})

            data["username"] = data.get("student_id").upper()

            dept = Department.objects.get(
                department_id__iexact=data.get("department_id")
            )

            data["department"] = int(dept.id)
            serializer = self.serializer_class(data=data, partial=False)

            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Account was registered"})
            return Response({"error": self.extract_error_handler(serializer.errors)})

        except Exception as e:
            print(e)
            return Response({"error": str(e)})
