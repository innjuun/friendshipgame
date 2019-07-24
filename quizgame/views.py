from django.shortcuts import render, redirect, resolve_url

# Create your views here.
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

<<<<<<< HEAD
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
=======
    elif request.method == 'GET':
        return render(request, '#')

def quizmaker_update(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(Quizmaker, pk=pk)
        user.count = request.POST.get('choice.id') ==
        user.contents = request.POST['contents']
        user.author = request.POST['author']
        user.save()
        return redirect(reverse('core:article_detail', kwargs={'pk': article.pk}))
    elif request.method == 'GET':
        article = get_object_or_404(Article, pk=pk)
        return render(request, 'core/article_create.html', {"article" : article})
>>>>>>> ca692aa363b753a0ba931fe971676602430aa950
