from django.db import models
from djongo import models
from django.contrib.auth.models import User

class Users(models.Model):
    _id = models.ObjectIdField(primary_key=True,  default='')
    email = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=25,default='')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Users'

class Jobs(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    designation = models.CharField(max_length=75, default='')
    company = models.CharField(max_length=75, default='')
    skills = models.CharField(max_length=75, default='')
    location = models.CharField(max_length=75, default='')
    summary = models.TextField(default='')
    email = models.CharField(max_length=100,default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.designation
    
    class Meta:
        db_table = 'Jobs'

class Contact(models.Model):
     _id = models.ObjectIdField()
     email = models.CharField(max_length=100)
     message = models.TextField()
     def __str__(self):
        return self.email
     class Meta:
        db_table = 'Contact'

# Create your models here.
