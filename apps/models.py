from django.db import models


class LearnTemplate(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	image = models.ImageField(upload_to="%d-%m-%y/", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.name)