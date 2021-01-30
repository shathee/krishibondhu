from django.db import models

# Create your models here.



class Crop(models.Model):
    
    name = models.CharField(max_length=50)
    bn_name = models.CharField(max_length=50)
    sc_name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)

    def __str__(self):
        return '{}'.format(self.name+'('+self.bn_name+')')


class CropSeason(models.Model):
    
    name = models.CharField(max_length=50)
    bn_name = models.CharField(max_length=50)
    time_period_en = models.CharField(max_length=50, blank=True, null=True)
    time_period_bn = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)

    def __str__(self):
        return '{}'.format(self.name+'('+self.bn_name+')')

    
class CropVariety(models.Model):
    
    name = models.CharField(max_length=50)
    bn_name = models.CharField(max_length=50)
    inventor = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)

    def __str__(self):
        return '{}'.format(self.name+'('+self.bn_name+')')

class CropStage(models.Model):
    
    name = models.CharField(max_length=50)
    bn_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(db_index=True, auto_now=True)

    def __str__(self):
        return '{}'.format(self.name+'('+self.bn_name+')')
