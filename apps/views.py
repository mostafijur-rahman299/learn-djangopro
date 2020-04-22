import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from tablib import Dataset

from .models import LearnTemplate, Photo
from apps.decorator import is_usersuper
from .forms import PhotoForm
from .resources import LearnTemplateResource


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


#custom mixin
class LearnMixin(object):
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['mix_title'] = "Hello Mixin"
		return context 

class LearnMixin2(object):
	def form_valid(self, form):
		pass 

	def form_invalid(self, form):
		pass


class LearnListView(LoginRequiredMixin, LearnMixin, ListView):
	model = LearnTemplate
	template_name = "apps/form.html"


class LearnDetailView(LoginRequiredMixin, LearnMixin, DetailView):
	model = LearnTemplate
	template_name = "apps/form.html"

# custom 404 and 500 errors
def handler404(request):
    return render(request, '404.html', {})

def handler500(request):
    return render(request, '500.html', {})


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PhotoForm()
    response = requests.get('http://127.0.0.1:8000/apps/learn-api/')
    print(response.status_code)
    return render(request, 'apps/photo_list.html', {'form': form, 'photos': photos})
    

def requests_test(requests):
	data = {
		'test': 'Hello world'
	}
	return JsonResponse(data)


def export_csv(request):
	learn_template_resources = LearnTemplateResource()
	qs = LearnTemplate.objects.all()
	dataset = learn_template_resources.export(qs)
	response = HttpResponse(dataset.csv, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="learntemplate.csv"'
	return response 

def export_excel(request):
	learn_template_resources = LearnTemplateResource()
	qs = LearnTemplate.objects.all()
	dataset = learn_template_resources.export(qs)
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename="learntemplate.xls"'
	return response

def import_new_data(request):
	if request.method == 'POST':
		import_file = request.FILES.get('import_file')
		file_format = request.POST.get('file_format')
		learntemplate_resources = LearnTemplateResource()
		dataset = Dataset()
		if file_format == 'excel':
			imported_file = dataset.load(import_file.read())
		if file_format == 'csv':
			imported_file = dataset.load(import_file.read().decode('utf-8'), format='csv')
		learntemplate_resources.import_data(dataset, raise_errors=True, dry_run=False)
	return redirect("learn-template")



