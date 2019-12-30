from djongo import models

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.username
