from django.db import models

class Groups(models.Model):
    group = models.CharField(max_length=50, default='Guest')
    
    def __str__(self) -> str:
        return self.group

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone = models.DecimalField(max_digits=9, decimal_places=0)
    
    def get_default():
        return Groups.objects.get_or_create(group='Guest')[0].id
    
    group = models.ForeignKey(Groups, on_delete=models.SET_DEFAULT, default=get_default)
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.username

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()
    
    def __str__(self) -> str:
        return str(self.data)

class Check(models.Model):
    date = models.DateField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    isHere = models.BooleanField(default=False)