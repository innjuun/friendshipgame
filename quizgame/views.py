from django.shortcuts import render, redirect, resolve_url

# Create your views here.
from django.shortcuts import render

from quizgame.models import Sign


def quizstart(request):
    if request.method == "GET":
        return render(request, "quizgame/quizmaker_main.html")
    else:
        username = request.POST['name']
        try:
            user = Sign.objects.get(name=username)
            return render(request, "quizgame/quizmaker_make.html", {'user': user})
        except:
            user = Sign.objects.create(name=username)
            return render(request, "quizgame/quizmaker_make.html", {'user': user})

def make_question(request):
    pass