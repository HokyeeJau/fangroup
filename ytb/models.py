from django.db import models

# Create your models here.
class background(models.Model):
    bg_date = models.DateField(null=False)
    bg_image = models.ImageField(upload_to='bg', verbose_name='background', null=False)

class portrait(models.Model):
    ptr_date = models.DateField(null=False)
    ptr_image = models.ImageField(upload_to='ptr', verbose_name='portrait', null=False)

class thumbnail(models.Model):
    thn_date = models.DateField(null=False)
    thn_image = models.ImageField(upload_to='thn', verbose_name='thumbnail', null=False)

class community(models.Model):
    cm_date = models.DateField(null=False)
    cm_content = models.TextField(null=False)
    cm_image = models.ImageField(upload_to='cm', verbose_name='community', null=True, blank=True)
