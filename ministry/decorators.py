from django.http import HttpResponse
from django.shortcuts import redirect
from api.models import User


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			user = request.user

			if user.role in allowed_roles:
				return view_func(request,*args, **kwargs)
			else:
				return HttpResponse("You are not authenticated to view this page!")

		return wrapper_func
	return decorator
