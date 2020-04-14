from django.urls import path
from .views import learn_template_view, LearnListView

urlpatterns = [
	path('learn-template/', learn_template_view, name='learn-template'),
	path('learn-list/', LearnListView.as_view(), name='learn-list')
]