from django.contrib import admin
from .models import video

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('vid_date', 'vid_title',)
    fieldsets = (
        ['Main', {
            'fields': ('vid_date', 'vid_title','vid_intro', 'admin',),
        }],
        ['Advance', {
            'classes': ('collapse', ),
            'fields': ('vid_bili_url', 'vid_baidu_url', 'vid_code', 'vid_cap_trans', 'vid_dial_trans', \
                        'vid_axis_prd', 'vid_cover_prd', 'vid_sup_prd',),
        }]
    )

admin.site.register(video, VideoAdmin)
