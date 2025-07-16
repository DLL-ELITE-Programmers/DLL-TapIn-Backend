from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from Organizations.serializers import OrganizationSerializer
from Organizations.models import Organization

class OrganizationViewset(ModelViewSet):
    queryset = Organization.objects.filter()
    serializer_class = OrganizationSerializer

    def list(self, req, *args, **kwargs):
        query = self.request.query_set

        data = self.serializer_class(self.queryset.all(), many=True)
        return Response(data.data)