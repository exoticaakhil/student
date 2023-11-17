from django.db import models

# Create your models here.

 
class student(models.Model):
    StudentName=models.CharField(max_length=255)
    Address=models.TextField(blank=True)
    Age=models.IntegerField()
    Emailid=models.EmailField()
    JoiningDate=models.DateField()
    Qualification=models.CharField(max_length=255)
    Gender=models.CharField(max_length=255)
    Mobile=models.CharField(max_length=255)
    Hobby=models.CharField(max_length=255,null=True)
    
