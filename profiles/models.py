from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from general.models import District

class Profile(models.Model):
	# Create your models here.

	# inlines = [ UserInline, ]

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mobile = models.CharField(max_length=15, blank=True, null=True)
	gender = models.CharField(max_length=2, choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Not Given')], default='N')
	profile_type = models.CharField(max_length=1,choices=[('F','Farmer'), ('A','Advisor')], blank=False, null=True)
	# district = models.ForeignKey(general_models.District, on_delete=models.SET_NULL, blank=False, null=True)
	district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=False, null=True)
	# division = models.ForeignKey(District.division, on_delete=models.SET_NULL, blank=False, null=True)

	def __str__(self):
		return '{}'.format(self.user)

	# def get_gender_display:

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

