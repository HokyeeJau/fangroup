from django.contrib import admin
from .models import video

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('vid_date', 'vid_title', 'vid_url',)
    fieldsets = (
        ['Main', {
            'fields': ('vid_date', 'vid_title', 'vid_url',),
        }],
        ['Advance', {
            'classes': ('collapse', ),
            'fields': ('vid_code', 'vid_intro', 'vid_cap_trans', 'vid_lines_trans', \
                        'vid_axis_prd', 'vid_cover_prd', 'vid_sup_prd', 'admin',),
        }]
    )

admin.site.register(video, VideoAdmin)
