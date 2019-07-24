from django.urls import path
from quizgame import views

app_name = 'quizgame'

urlpatterns = [
    path('', views.quizstart, name='quizstart'),
    path('<int:user_id>/<int:q>/', views.make_question, name="make_question")
    ]