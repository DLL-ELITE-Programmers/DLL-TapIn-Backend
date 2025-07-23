from rest_framework.response import Response

from BaseAuth.views import BaseAuthModelViewset
from Organizations.models import Organization
from Organizations.serializers import OrganizationSerializer


class OrganizationViewset(BaseAuthModelViewset):
    queryset = Organization.objects.filter()
    serializer_class = OrganizationSerializer

    def list(self, req, *args, **kwargs):
        query = self.request.query_set

        data = self.serializer_class(self.queryset.all(), many=True)
        return Response(data.data)

    def create(self, request, *args, **kwargs):
        try:
            data = request.data

            serialize = self.serializer_class(data, many=True)

            if serialize.is_valid():
                serialize.save()
                return Response({"message": "Event created successfully"})

            return Response({"error": self.extract_error_handler(serialize.errors)})

        except Exception as e:
            return Response({"error": str(e)})
