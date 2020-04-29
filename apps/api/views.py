from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from apps.models import LearnTemplate 
from .serializers import LearnTemplateSerializer
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Q
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


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
	queryset = LearnTemplate.objects.filter(Q(name__icontains='s')|Q(name__icontains='m'))
	serializer_class = LearnTemplateSerializer


class LearnTemplateAPIViewFiltering(generics.ListAPIView):
	serializer_class = LearnTemplateSerializer
	queryset = LearnTemplate.objects.all()
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['name', 'created_at']
	search_fields = ['name', 'description']
	ordering_fields = ['name', 'description']



