from import_export import resources
from .models import LearnTemplate


class LearnTemplateResource(resources.ModelResource):
	class Meta:
		model = LearnTemplate
		