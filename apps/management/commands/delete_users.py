from django.core.management.base import BaseCommand 
from django.contrib.auth.models import User 


class Command(BaseCommand):
	help = 'Delete users'

	def add_arguments(self, parser):
		# arbitary list of argument
		parser.add_argument('user_id', nargs='+', type=int, help="User id")

	def handle(self, *args, **kwargs):
		user_ids = kwargs['user_id']
		for user_id in user_ids:
			try:
				user = User.objects.get(pk=user_id)
				user.delete()
				self.stdout.write("User of %s id is delete successfully:)" % user_id)
			except User.DoesNotExist:
				self.stdout.write("User with id %s does not exist!" % user_id)