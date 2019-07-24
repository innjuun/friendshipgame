from django.contrib import admin

# Register your models here.
from quizgame.models import Sign

@admin.register(Sign)
class SignAdmin(admin.ModelAdmin):
    list_display=['name','code']