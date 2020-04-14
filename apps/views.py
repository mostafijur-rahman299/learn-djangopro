from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import user_passes_test

from .models import LearnTemplate
from apps.decorator import is_usersuper


def is_active(user):
	return user.is_active

@user_passes_test(is_active)
@is_usersuper
def learn_template_view(request):
	qs = LearnTemplate.objects.all()
	context = {
		'queryset': qs,
		'value': 'https://www.example.org/foo?a=b&c=d'
	}
	return render(request, "apps/learn_templates.html", context)


