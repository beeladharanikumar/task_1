from django.db import models
import datetime
class Register(models.Model):
    first_name = models.CharField(max_length=30,null=True,default='')
    last_name = models.CharField(max_length=30,null=True,default='')
    user_name = models.CharField(max_length=20,null=True,blank=False,default='',unique=True)
    email = models.EmailField(null=True,default='',unique = True)
    phone_number = models.CharField(max_length=12,null=True,blank=False,default='',unique=True)
    password = models.CharField(max_length=18,null=True,blank=False,default='')
    gender_choice = [
        ('male','male'),
        ('female','female'),
        ('not specified','not specified')
    ]
    gender = models.CharField(max_length=20,choices=gender_choice,null=True,blank=False,default='')

class Login(models.Model):
    
    user_name = models.CharField(max_length=30,null=True,blank=False,default="user_name")
    password = models.CharField(max_length=30,null=True,blank=False,default='passcode')
    login_time = models.DateTimeField(default=datetime.datetime.now())
    login_status = models.CharField(max_length=30,default="register")


class temp(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)

class tasks(models.Model):
    user = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    task = models.TextField(max_length=100,null=True)


class ParentModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
    description = models.TextField()

class file_upload(models.Model):
    file = models.FileField(upload_to="C:/Users/bdharani/Desktop/task/project/register/uploaded_files")
    file_time = models.DateTimeField(default=datetime.datetime.now())