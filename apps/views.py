from django.shortcuts import render
from .models import LearnTemplate


def learn_template_view(request):
	qs = LearnTemplate.objects.all()
	context = {
		'queryset': qs,
		'value': 'https://www.example.org/foo?a=b&c=d'
	}
	return render(request, "apps/learn_templates.html", context)
