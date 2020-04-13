from django.utils.deprecation import MiddlewareMixin
from datetime import datetime 


class LearnMiddleware(MiddlewareMixin):
	def process_request(self, request):
		request.current_time = datetime.now() 
		request.current_name = "sajib"
		print("Hello world")