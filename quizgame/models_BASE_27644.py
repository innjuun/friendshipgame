from django.db import models

# Create your models here.
class Quizmaker():
    username = models.CharFields(max_length=20)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
class Quizsolver():
    username = models.CharField(max_length=20)

class Answer():

    first = models.CharField(max_length=1)
    second = models.CharField(max_length=1)
    third = models.CharField(max_length=1)
    fourth = models.CharField(max_length=1)
    fifth = models.CharField(max_length=1)
    sixth = models.CharField(max_length=1)
    seventh = models.CharField(max_length=1)
    eighth = models.CharField(max_length=1)
    nineth = models.CharField(max_length=1)
    tenth = models.CharField(max_length=1)