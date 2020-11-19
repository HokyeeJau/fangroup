from django.contrib import admin
from .models import background, portrait, thumbnail, community

# Register your models here.
class BackgroundAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('bg_date', )
    fieldsets = (
        ['Main', {
            'fields':('bg_date',),
        }],
        ['Advance', {
            'classes':('collapse', ), #CSS
            'fields':('bg_image',),
        }]
    )

class PortraitAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('ptr_date', )
    fieldsets = (
        ['Main', {
            'fields': ('ptr_date',),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('ptr_image',),
        }]
    )

class ThumbnailAmdin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('thn_date', )
    fieldsets = (
        ['Main', {
            'fields': ('thn_date',),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('thn_image', ),
        }]
    )

class CommunityAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('cm_date',)
    fieldsets = (
        ['Main', {
            'fields': ('cm_date', 'cm_content', )
        }],
        ['Advance', {
            'classes': ('collapse', ),
            'fields': ('cm_image',),
        }]
    )

admin.site.register(background, BackgroundAdmin)
admin.site.register(portrait, PortraitAdmin)
admin.site.register(thumbnail, ThumbnailAmdin)
admin.site.register(community, CommunityAdmin)
