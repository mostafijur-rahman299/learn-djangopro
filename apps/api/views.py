from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from apps.models import LearnTemplate 
from .serializers import LearnTemplateSerializer
from rest_framework.response import Response
from rest_framework import permissions


class LearnTemplateViewset(viewsets.ViewSet):

	def list(self, request):
		queryset = LearnTemplate.objects.all()
		serializer = LearnTemplateSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = LearnTemplate.objects.all()
		obj = get_object_or_404(queryset, pk=pk)
		serializer = LearnTemplateSerializer(obj)
		return Response(serializer.data)


class LearnTemplateModelViewSet(viewsets.ModelViewSet):
	queryset = LearnTemplate.objects.all()
	serializer_class = LearnTemplateSerializer

	def get_serializer_context(self):
		context = super().get_serializer_context()
		action = self.action

		if (action == 'list'):
			context['fields'] = ('id', 'name', 'description',)
		elif (action == 'create'):
			context['fields'] = ('id',)
		elif (action == 'retrieve'):
			context['fields'] = ('name', 'description')
		return context
