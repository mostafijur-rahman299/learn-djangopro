from django.test import TestCase, Client
from .models import LearnTemplate
from django.urls import reverse


class TestLearnTemplate(TestCase):
	def setUp(self):
		self.learnproject = LearnTemplate.objects.create(
			name = 'd',
			mobile_number = '+8801789929182',
		)
		self.client = Client()
		self.list_url = reverse('learn-template')
		self.detail_url = reverse('learn-detail', kwargs={'pk': 1})

	def test_assigned_description(self):
		self.assertEquals(self.learnproject.description, 'hello world')

	def test_learn_template_list(self):
		response = self.client.get(self.list_url)
		self.assertEquals(response.status_code, 200)

	def test_learn_template_detail(self):
		response = self.client.get(self.detail_url)
		self.assertEquals(response.status_code, 404)

	def test_learn_template_create(self):
		url = reverse('add')
		response = self.client.post(url, {
			'name': 'test',
			'mobile_number': '+8801789929182'
		})
		p = LearnTemplate.objects.get(id=2)
		self.assertEquals(p.name, 'test')
		

