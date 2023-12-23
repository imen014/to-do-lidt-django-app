from django.shortcuts import render
from my_to_do_list.forms import TodolistForm
from my_to_do_list.models import MyToDoList


def showForm(request):
    myform = TodolistForm()
    todolistMaker = MyToDoList()
    if request.method == "POST":
         myform = TodolistForm(request.POST)
         if  myform.is_valid():
              task_title = myform.cleaned_data['task_title']
              task_content = myform.cleaned_data['task_content']
              creator_email = myform.cleaned_data['creator_email']
              todolistMaker.task_title = task_title
              todolistMaker.task_content = task_content
              todolistMaker.creator_email = creator_email
              todolistMaker.save()
              message = "data saved succeffully !"
         else:
              message = "form is not valid !"
    else:
         message = "method id not post !"

    return render(request,
                  'my_to_do_list/showForm.html',
                  {'myform':myform,
                   'message':message})

def get_task(request):
     tasks = MyToDoList.objects.all()
     return render(request,
                   'my_to_do_list/get_tasks.html',
                   {'tasks':tasks})
