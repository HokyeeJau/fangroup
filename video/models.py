from django.db import models

# Create your models here.
class video(models.Model):
    # video title, published date, url, introduction
    vid_date = models.DateField()
    vid_title = models.CharField(max_length=20)
    vid_url = models.URLField()
    vid_code = models.CharField(max_length=4)
    vid_intro = models.CharField(max_length=100)

    # caption translators, lines translators,
    vid_cap_trans = models.CharField(max_length=100)
    vid_lines_trans = models.CharField(max_length=100)

    # video axis producers, video cover producers, video suppress producers
    vid_axis_prd = models.CharField(max_length=100)
    vid_cover_prd = models.CharField(max_length=100)
    vid_sup_prd = models.CharField(max_length=100)

    admin = models.EmailField()
