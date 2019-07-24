from django.db import models

# Create your models here.
class Sign(models.Model):
    name = models.CharField(max_length=5)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    sign = models.ForeignKey(Sign, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
