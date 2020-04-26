import requests, datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from tablib import Dataset
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.urls import reverse
from django.utils import translation
from django.utils.translation import gettext as _
from django.utils.translation import ngettext

from .models import LearnTemplate, Photo
from apps.decorator import is_usersuper
from .forms import PhotoForm
from .resources import LearnTemplateResource


def is_active(user):
	return user.is_active

@user_passes_test(is_active)
@is_usersuper
def learn_template_view(request):
	if 'lang' in request.GET:
		translation.activate(request.GET.get('lang'))
	qs = LearnTemplate.objects.all()
	title = _("Hello, how are you?")
	date = datetime.datetime.now()
	month = _(date.strftime("%B"))
	day = _(date.strftime("%A"))
	today = _("Today is  %(month)s %(day)s") %{'day':day, 'month':month}

	count = 1
	if count == 1:
		name = _("man")
	else:
		name = _("mans")
	text = ngettext(
    	'There is %(count)d %(name)s available.',
    	'There are %(count)d %(name)s available.',count) % {'count': count,'name': name}

	context = {
		'queryset': qs,
		'value': 'https://www.example.org/foo?a=b&c=d',
		'title': title,
		'today': today,
		'page': text
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

# Render pdf
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    # pdf name generate with date    
    date = datetime.date.today()
    tmpName = template_src.split('.')[0]
    pdfName=tmpName + "-"+ str(date)
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename='+pdfName+'.pdf'        
        return response
    return HttpResponse('We had some errors')


def learn_pdf(request):
    qs = LearnTemplate.objects.all()
    context = {
        'qs': qs,
        } 
    pdf = render_to_pdf("apps/html_to_pdf.html", context)
    download = request.GET.get('download')
    if download:
        return pdf 
    return HttpResponse(pdf, content_type='application/pdf')
    
