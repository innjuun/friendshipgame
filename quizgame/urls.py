from django.urls import path
from quizgame import views

app_name = 'quizgame'

urlpatterns =[
    path('', views.quizstart, name='quizstart' ),
]