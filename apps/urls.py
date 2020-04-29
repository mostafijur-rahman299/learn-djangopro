from django.urls import path
from .views import (learn_template_view, 
	LearnListView, 
	learn_detail,
	handler500, 
	handler404, 
	photo_list, 
	requests_test,
	export_csv,
	export_excel,
	import_new_data,
	learn_pdf,
	learn_template_list,
	learn_template_detail)
from django.conf.urls import handler404, handler500
from rest_framework.urlpatterns import format_suffix_patterns
from apps.api.views import LearnTemplateAPIViewFiltering

urlpatterns = [
	path('learn-template/', learn_template_view, name='learn-template'),
	path('learn-list/', LearnListView.as_view(), name='learn-list'),
	path('learn-detail/<int:id>/', learn_detail, name='learn-detail'),
	path('learn-api/', requests_test, name='learn-api'),
	path('photo-list/', photo_list, name='photo-list'),
	path('export-csv/', export_csv, name="export-csv"),
	path('export-excel/', export_excel, name="export-excel"),
	path('import-data/', import_new_data, name="import-data"),
	path('download-pdf/', learn_pdf, name="download-pdf"),
	path('new-learn-api/', learn_template_list, name="new-learn-api"),
	path('new-learn-api/<int:id>/', learn_template_detail, name="new-learn-api-detail"),
	path('learn-cbv-api/', LearnTemplateAPIViewFiltering.as_view(), name='learn-api-cbv')
]

handler404 = handler404
handler500 = handler500

