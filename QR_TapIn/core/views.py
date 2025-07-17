from rest_framework.status import HTTP_404_NOT_FOUND
from django.http import HttpResponse

# Create your views here.

def main(request):
    return HttpResponse("<h1>Miss mo na? Kaso miss ka ba?</h1>")

def _404(request):
    return HttpResponse("<h1>Bakit mo kasi hinahanap ang wala na. Awat na kase.</h1>", status=HTTP_404_NOT_FOUND)