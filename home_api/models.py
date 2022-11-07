from django.db import models
from django.contrib.auth.models import User

class Groups(models.Model):
    name = models.CharField(max_length=255, default='Guest')
    user = models.ManyToManyField(User)
    
    def __str__(self) -> str:
        return self.group

class HomeWork(models.Model):
   name = models.CharField(max_length=255)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='homework')

   def __str__(self):
        return self.name

class Task(models.Model):
    homework = models.ForeignKey(HomeWork, on_delete=models.CASCADE, related_name='task')
    name = models.CharField(max_length=255)
    attempt = models.IntegerField()
    isSolved = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.homework)

class Check(models.Model):
    date = models.DateField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    isHere = models.BooleanField(default=False)