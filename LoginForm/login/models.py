from __future__ import unicode_literals

from django.db import models

# Create your models here.
class login_data(models.Model):
	name=models.CharField(max_length=50,blank=False,null=False)
	mobile=models.IntegerField(default=0)
	city=models.CharField(max_length=10,blank=False,null=False)
	gender=models.CharField(max_length=10,blank=False,null=False)
	email=models.CharField(max_length=50,blank=False,null=False)
	password=models.CharField(max_length=10,null=False,blank=False)
	description=models.CharField(max_length=100,blank=False,null=False)

	
