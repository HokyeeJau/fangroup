from django.contrib import admin
from .models import rsc_admin

# Register your models here.
class RscAdmin(admin.ModelAdmin):
    list_display = ('admin_name', 'admin_email', 'admin_contact')
    fields = [
        'admin_email', 'admin_pwd', 'admin_name',
        'admin_contact', 'admin_rsc', 'admin_ip'
    ]

admin.site.register(rsc_admin, RscAdmin)
