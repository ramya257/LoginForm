from django.contrib import admin
from .models import *
# Register your models here.
class login_dataAdmin(admin.ModelAdmin):
	list_display=["name","mobile","gender","email"]
admin.site.register(login_data,login_dataAdmin)
			
