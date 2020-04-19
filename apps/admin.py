from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import LearnTemplate, Photo


class LearnTemplateAdmin(SimpleHistoryAdmin):
	history_list_display = ['status',]

admin.site.register(LearnTemplate, LearnTemplateAdmin)

admin.site.register(Photo)
