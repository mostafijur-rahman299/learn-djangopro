from django.urls import path
from .views import learn_template_view

urlpatterns = [
	path('learn-template/', learn_template_view, name='learn-template')
]