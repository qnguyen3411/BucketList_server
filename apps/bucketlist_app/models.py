from django.db import models

class Task(models.Model):
    objective = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    
