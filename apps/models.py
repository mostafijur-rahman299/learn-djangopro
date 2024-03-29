from django.db import models
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from geoposition.fields import GeopositionField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse

def validate_image(image):
	file_size = image.size
	limit_mb = 10 * 1024 
	if file_size > limit_mb:
	 	raise ValidationError(_("Maximum size of file is 10 mb"))


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
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=120, help_text=_("Your name must have to be unique!"))
	mobile_number = PhoneNumberField(blank=True, default="+88")
	# position = GeopositionField()
	description = models.TextField(blank=True, null=True)
	image = models.FileField(upload_to="%d-%m-%y/", blank=True, null=True, validators=[validate_image])
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	history = HistoricalRecords()

	objects = LearnTemplateManager()

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self, *args, **kwargs):
		return reverse('learn-detail', kwargs={'id': self.id})	

	# reduce image size
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		self.description = "hello world"
		if self.image:
			img = Image.open(self.image.path)
			if img.height > 300 or img.width > 300:
				output_size = (300, 300)
				img.thumbnail(output_size)
				img.save(self.image.path)


# Crop and reduce image 
class Photo(models.Model):
    file = models.ImageField()
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)