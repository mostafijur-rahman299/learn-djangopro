from django.urls import path
from .views import (learn_template_view, 
	LearnListView, 
	handler500, 
	handler404, 
	photo_list, 
	requests_test,
	export_csv,
	export_excel,
	import_new_data,
	learn_pdf)
from django.conf.urls import handler404, handler500

urlpatterns = [
	path('learn-template/', learn_template_view, name='learn-template'),
	path('learn-list/', LearnListView.as_view(), name='learn-list'),
	path('learn-api/', requests_test, name='learn-api'),
	path('photo-list/', photo_list, name='photo-list'),
	path('export-csv/', export_csv, name="export-csv"),
	path('export-excel/', export_excel, name="export-excel"),
	path('import-data/', import_new_data, name="import-data"),
	path('download-pdf/', learn_pdf, name="download-pdf"),
]

handler404 = handler404
handler500 = handler500