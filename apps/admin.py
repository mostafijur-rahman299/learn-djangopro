from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from .models import LearnTemplate, Photo


class LearnTemplateAdmin(ImportExportModelAdmin):
	class Meta:
		model = LearnTemplate

admin.site.register(LearnTemplate, LearnTemplateAdmin)

admin.site.register(Photo)
