import random

from django.http import HttpResponse
from rest_framework.status import HTTP_404_NOT_FOUND

# Create your views here.


def main(request):
    return HttpResponse("<h1>Miss mo na? Kaso miss ka ba?</h1>")


def _404(request):
    responses = [
        "Bakit mo kasi hinahanap ang wala na, Awat na kase.",
        "Sanaol hinahanap, ikaw kaya hahanapin din?",
        "Yung tipong akala mo may pag-asa pa, pero it's a prank.",
        "Kung ang isang bansa ay may watawat, bakit mo pa hinahanap?",
        "flag{sorry hindi ito ang flag}",
        "Yung akala mo nakita mo na, pero nagising kang bigla.",
        "Swerte kunyare, pero malas talaga.",
        "May pang gala ka nga, wala ka namang kasama, sana ako na lang.",
        "Kung ang pusa ay may syam na buhay, sana ikaw na lang habang buhay.",
        "Pre, di ako lasing, pero bakit sya pa rin.",
    ]
    response = responses[random.randint(0, len(responses) - 1)]
    return HttpResponse(
        f"<h1>{response}</h1>",
        status=HTTP_404_NOT_FOUND,
    )
