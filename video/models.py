from django.db import models

# Create your models here.
class video(models.Model):
    # video title, published date, url, introduction
    vid_date = models.DateField()
    vid_title = models.CharField(max_length=20)
    vid_bili_url = models.URLField(null=True, blank=True)
    vid_baidu_url = models.URLField(null=True, blank=True)
    vid_code = models.CharField(max_length=4, null=True, blank=True)
    vid_intro = models.CharField(max_length=100)

    # caption translators, dialogue translators,
    vid_cap_trans = models.CharField(max_length=100, null=True, blank=True)
    vid_dial_trans = models.CharField(max_length=100, null=True, blank=True)

    # video axis producers, video cover producers, video suppress producers
    vid_axis_prd = models.CharField(max_length=100, null=True, blank=True)
    vid_cover_prd = models.CharField(max_length=100, null=True, blank=True)
    vid_sup_prd = models.CharField(max_length=100, null=True, blank=True)

    admin = models.EmailField()
