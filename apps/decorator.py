from django.http import HttpResponseRedirect
from functools import wraps


def is_usersuper(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		if request.user.is_superuser:
			print("done")
			return function(request, *args, **kwargs)
		else:
			return HttpResponseRedirect("/")
	# wrap.__doc__ = function.__doc__
	# wrap.__name__ = function.__name__
	return wrap 

