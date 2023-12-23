from django.db import models

class MyToDoList(models.Model):
    task_title = models.CharField(max_length=255)
    task_content = models.CharField(max_length=255)
    creator_email = models.EmailField()
