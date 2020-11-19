from django.contrib import admin
from .models import schedule

# Register your models here.

class ScheduleAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('sche_date', 'sche_title', 'sche_rsc', 'admin',)
    fieldsets = (
        ['Main',{
            'fields':('sche_date', 'sche_title', 'sche_content', 'sche_rsc'),
        }],
        ['Advance',{
            'classes':('collapse', ), #CSS
            'fields':('admin',),
        }]
    )
    # def has_change_permission(self, request, obj=None):
    #     has_class_permission = super(ScheduleAdmin, self).has_change_permission(request, obj)
    #     if not has_class_permission:
    #         return False
    #     if obj is not None and request.user.id != obj.author.id:
    #         return False
    #     return True
    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.author = request.user
    #     obj.save()

admin.site.register(schedule, ScheduleAdmin)
