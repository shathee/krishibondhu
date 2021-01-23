from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	# Create your models here.

	# inlines = [ UserInline, ]

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# first_name = models.CharField(max_length=50, blank=False, null=False)
	# last_name = models.CharField(max_length=50, blank=True, null=True)
	profile_type = models.CharField(max_length=1,choices=[('F','Farmer'), ('A','Advisor')], default='F',)


	def __str__(self):
		return 'Profile: {}'.format(self.user)

