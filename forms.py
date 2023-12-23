from django.forms import ModelForm
from my_to_do_list.models import MyToDoList

class TodolistForm(ModelForm):
    class Meta:
        model = MyToDoList
        fields = ['task_title','task_content','creator_email']
        