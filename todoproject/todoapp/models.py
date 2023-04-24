from django.db import models

# Create your models here.
#3
class TodoListItem(models.Model):
    content = models.TextField() 