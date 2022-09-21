from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone = models.PhoneNumberField()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()