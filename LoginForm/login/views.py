from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import login_data
import requests
import random
# Create your views here.
def login(request):
	response_json={}
	if request.method=='GET':
		return render(request,"index.html",{})
	else:
		for x,y in request.POST.items():
			print "key,value",x,":",y
		name=str(request.POST.get('name'))
		password=str(request.POST.get('password'))
		gender=str(request.POST.get('gender'))
		email=str(request.POST.get('email'))
		description=str(request.POST.get('description'))
		city=str(request.POST.get('city'))
		mobile=int(request.POST.get('mobile'))
		login=login_data.objects.create(name=name,password=password,gender=gender,email=email
			,description=description,city=city,mobile=mobile)
		login.save()
		return render(request,"index.html",{}) 