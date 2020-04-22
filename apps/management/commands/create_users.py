from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

# Handling Arguments
class Command(BaseCommand):
	help = 'Create random users'

	def add_arguments(self, parser):
		parser.add_argument('total', type=int, help='Indicates the number of users to be created')

		# optional arguments 
		parser.add_argument('-p', '--prefix', type=str, help='Define username prefix')

		# flag boolean arguments 
		parser.add_argument('-a', '--admin', action="store_true", help="Create admin account")

	def handle(self, *args, **kwargs):
		total = kwargs['total']
		prefix = kwargs['prefix']
		admin = kwargs['admin']
		if not total:
			total = 1
		for i in range(total):
			if prefix:
				username = "{prefix}_{random_string}".format(prefix=prefix, random_string=get_random_string())
			else:
				username = get_random_string()
			if admin:
				User.objects.create_superuser(username=username, email='', password='mahmud678')
			else:
				User.objects.create_user(username=username, email='', password='mahmud678')