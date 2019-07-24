from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def quizstart(request):
    return render(request, 'quizgame/quizmaker_main.html')