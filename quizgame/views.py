from django.shortcuts import render

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

    elif request.method == 'GET':
        return render(request, '#')

def quizmaker_update(request, pk):

    if request.method == 'POST':
        user = get_object_or_404(Quizmaker, pk=pk)
        user.count = request.POST.get('choice.id')

        user.save()
        return redirect(reverse('core:article_detail', kwargs={'pk': article.pk}))
    elif request.method == 'GET':
        article = get_object_or_404(Article, pk=pk)
        return render(request, 'core/article_create.html', {"article" : article})
