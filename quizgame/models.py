from django.db import models

# Create your models here.
<<<<<<< HEAD
class Sign(models.Model):
    name = models.CharField(max_length=5)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    sign = models.ForeignKey(Sign, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
=======

class Quizmaker():
    username = models.CharFields(max_length=20)

class Quizsolver():
    username = models.CharField(max_length=20)

class Answer():
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
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

>>>>>>> ca692aa363b753a0ba931fe971676602430aa950
