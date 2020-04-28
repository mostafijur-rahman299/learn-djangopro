from rest_framework import serializers
from apps.models import LearnTemplate
from django.utils.timesince import timesince


class LearnTemplateSerializer(serializers.ModelSerializer):
	url = serializers.CharField(source='get_absolute_url',	read_only=True)
	timesince = serializers.SerializerMethodField()
	date_display = serializers.SerializerMethodField()

	class Meta:
		model = LearnTemplate
		fields = (
			'user', 'id', 'name', 'mobile_number', 'description', 
			'image', 'created_at', 'updated_at', 'url', 'date_display', 'timesince')
		# read_only_fields = ('name', 'user')
		depth = 1

	def validate(self, value):
		print(value)
		return value

	def get_timesince(self, obj):
		return timesince(obj.created_at) + " ago"

	def get_date_display(self, obj):
		return obj.created_at.strftime("%d %b %Y at %I:%M %p")


