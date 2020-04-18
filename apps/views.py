from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import LearnTemplate, Photo
from apps.decorator import is_usersuper
from .forms import PhotoForm


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
    return render(request, 'apps/photo_list.html', {'form': form, 'photos': photos})
    