from BaseAuth.mixins import CustomMixins
from BaseAuth.paginator import TenRowPaginator

from rest_framework import viewsets
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class BaseAuthModelViewset(viewsets.ModelViewSet, CustomMixins):
  permission_classes = [IsAuthenticated]
  authentication_classes = [JWTAuthentication]
  pagination_class = TenRowPaginator

  def list(self, req, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())
    params = self.request.query_params

    if "paginate" in params:
      page = self.paginate_queryset(queryset)

      if page is not None:
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)

  def extract_error_handler(self, err):
    if isinstance(err, dict):
      for key, value in err.items():
        if isinstance(value, list) and value:
          return str(value[0])
        else:
          return self.extract_error_handler(value)
    return str(err)


def custom_not_authorized(exc, context):
  response = exception_handler(exc, context)

  if isinstance(exc, NotAuthenticated):
    return Response(
      {
        "error": "You're not authorized to gather information here",
        "code": "Miss na kita baby ko, plz balik ka na.",
      }
    )
  return response
