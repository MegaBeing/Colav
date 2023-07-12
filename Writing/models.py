from django.db import models


# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=25,null=False)
    last_name = models.CharField(max_length=25,null=False)
    user_name = models.CharField(max_length=25,null=False)
    password = models.CharField(max_length=100,null=False)

class Section(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)

class Page(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    section = models.ForeignKey(Section,on_delete=models.CASCADE)

