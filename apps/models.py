from django.db import models


class LearnTemplateQueryset(models.QuerySet):
	def latest_two(self):
		return self.order_by("-created_at")[:2]

	def new_year(self):
		return self.filter(created_at__year=2020)


class LearnTemplateManager(models.Manager):
	def get_queryset(self):
		return LearnTemplateQueryset(self.model, self._db)

	def latest_two(self):
		return self.get_queryset().latest_two()

	def new_year(self):
		return self.get_queryset().new_year()


class LearnTemplate(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	image = models.ImageField(upload_to="%d-%m-%y/", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = LearnTemplateManager()

	def __str__(self):
		return str(self.name)