from django.db import models

# Create your models here.
class schedule(models.Model):
    sche_date = models.DateField()
    sche_title = models.CharField(max_length=20)
    sche_content = models.TextField()
    sche_rsc = models.URLField()
    admin = models.EmailField()
