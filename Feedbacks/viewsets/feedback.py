from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Accounts.models import User
from BaseAuth.views import BaseAuthModelViewset
from Feedbacks.models import Feedback
from Feedbacks.serializers import FeedbackSerializer


class FeedbackViewset(BaseAuthModelViewset):
    permission_classes = [AllowAny]
    queryset = Feedback.objects.filter()
    serializer_class = FeedbackSerializer

    def list(self, request, *args, **kwargs):
        params = self.request.query_params

        if params.get("user"):
            user = User.objects.get(username__iexact=params.get("u"))
            self.queryset = Feedback.objects.filter(username__exact=user.id)

        data = self.serializer_class(self.queryset, many=True)
        return Response(data.data)

    def create(self, request, *args, **kwargs):
        req = request.data

        data = self.serializer_class(req, partial=True)

        if data.is_valid():
            data.save()
            return Response({"message": "Feedback added"})
        return Response({"error": self.extract_error_handler(data.error)})
