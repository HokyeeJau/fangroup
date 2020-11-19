from django.db import models

# Create your models here.
class rsc_admin(models.Model):
    admin_email = models.EmailField()
    admin_pwd = models.CharField(max_length=30)
    admin_name = models.CharField(max_length=10)
    admin_contact = models.CharField(max_length=30)
    admin_rsc = models.PositiveSmallIntegerField()
    admin_ip = models.CharField(max_length=16)
