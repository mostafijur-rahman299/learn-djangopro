from django.urls import path
from .views import learn_template_view, LearnListView, handler500, handler404
from django.conf.urls import handler404, handler500

urlpatterns = [
	path('learn-template/', learn_template_view, name='learn-template'),
	path('learn-list/', LearnListView.as_view(), name='learn-list')
]

handler404 = handler404
handler500 = handler500