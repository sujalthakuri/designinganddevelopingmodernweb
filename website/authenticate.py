from django.shortcuts import render,redirect
from. models import Users, admin
from django.contrib import messages

class Authenticate:
	def auth_user(function):
		def wrap(request):
				if(request.session['username']!=None):

					return function(request)
				else:
					messages.warning(request,"Please login...")
					return redirect("/")
		return wrap

	def auth_admin(function):
		def wrap(request):
			try:
				admin.objects.get(username = request.sesion['adminname'])
				
				return function(request)
			except:
				messages.warning(request,"Please Authorize Login")
				return redirect("/")