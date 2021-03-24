from django.db import models

# Create your models here.


class ProblemTopic(models.Model):
    
    name = models.CharField(max_length=50)
    bn_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.name)

class Problem(models.Model):
    
    name = models.CharField(max_length=50)
    bn_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)


class LandType(models.Model):
    
    name = models.CharField(max_length=50)
    bn_name = models.CharField(max_length=50, default='')
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)

class SoilType(models.Model):
    
    name = models.CharField(max_length=50)
    bn_name = models.CharField(max_length=50, default='')
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.name, self.bn_name)