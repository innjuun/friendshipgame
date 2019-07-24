from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Quizmaker, Quizsolver



def quizmaker_create(request):
    if request.method == 'POST':
        print(request.POST)
        user = Quizmaker()
        user.username = request.POST['name']


        user.save()
        return redirect(reverse('#', kwargs={'pk': user.id}))



def quizstart(request):
    return render(request, 'quizgame/quizmaker_main.html')