from django.db import models



# Create your models here.

class Division(models.Model):
	name = models.CharField(max_length=15, blank=False, null=False)
	bn_name = models.CharField(max_length=15, blank=True, null=True)
	def __str__(self):
		return '{}'.format(self.name)


class District(models.Model):
	division = models.ForeignKey(Division, on_delete=models.CASCADE)
	name = models.CharField(max_length=15, blank=False, null=False)
	bn_name = models.CharField(max_length=15, blank=True, null=True)
	lat = models.TextField(max_length=50, blank=True, null=True)
	lon = models.TextField(max_length=50, blank=True, null=True)
	website = models.URLField( blank=True, null=True)
	metropolitan = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='N', blank=True, null=True)
	
	def __str__(self):
		return '{}'.format(self.name)

class Upazila(models.Model):
	district = models.ForeignKey(District, on_delete=models.CASCADE, default='1')
	name = models.CharField(max_length=15, blank=False, null=False)
	bn_name = models.CharField(max_length=15, blank=True, null=True)
	def __str__(self):
		return '{}'.format(self.name)

class Union(models.Model):
	name = models.CharField(max_length=15, blank=False, null=False, default='1')
	bn_name = models.CharField(max_length=15, blank=True, null=True)
	def __str__(self):
		return '{}'.format(self.name)
