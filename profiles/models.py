from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	# Create your models here.

	# inlines = [ UserInline, ]

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mobile = models.CharField(max_length=15, blank=True, null=True)
	gender = models.CharField(max_length=2, choices=[('M', 'Male'), ('F', 'Female')], default='M')
	profile_type = models.CharField(max_length=1,choices=[('F','Farmer'), ('A','Advisor')], default='F',)


	def __str__(self):
		return '{}'.format(self.user)



