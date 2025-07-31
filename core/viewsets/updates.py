from rest_framework.response import Response
from rest_framework.views import APIView


class UpdatesAPI(APIView):
    def get(self, req):
        return Response(
            {
                "message": "Thie update was created for test",
                "version": "0.1.2",
                "new": ["Walang bago, ikaw pa rin"],
                "link": "https://google.com",
                "require": True,
            }
        )
