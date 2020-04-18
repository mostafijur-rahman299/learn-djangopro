from django.urls import path
from .views import learn_template_view, LearnListView, handler500, handler404, photo_list
from django.conf.urls import handler404, handler500

urlpatterns = [
	path('learn-template/', learn_template_view, name='learn-template'),
	path('learn-list/', LearnListView.as_view(), name='learn-list'),
	path('photo-list/', photo_list, name='photo-list')
]

handler404 = handler404
handler500 = handler500