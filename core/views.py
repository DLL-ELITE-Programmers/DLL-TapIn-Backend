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
        "Kung miss mo, e di wow.",
        "Uy, naghahanap pa rin hahaha.",
        "Wag mong hintayin, agawin mo na agad.",
        "Kung ang mga ibon ay lumilupad, susunod ka na.",
        "Minsan na nga lang swertehin, nagising pa.",
        "Sabi ng bestfriend ko, pangit sya, pero sinabihan ko sya ng maganda, anong next step?",
        "Hindi masamang umasa, lalo na kung ***** ka.",
        "Mas masakit pa sa nahulog mo ung natitirang pamasahe mo, ung walang natirang feelings para sayo.",
        "Di ba sabi mo, di mo ko iiwan. Di pababayaang ako'y mag-isa. Di ba sabi mo sabay tayong tatanda, bakit bigla ka na lang nanjaan, sa kabilang bahay.",
    ]
    response = responses[random.randint(0, len(responses) - 1)]
    return HttpResponse(
        f"<h1>{response}</h1>",
        # status=HTTP_404_NOT_FOUND,
    )
