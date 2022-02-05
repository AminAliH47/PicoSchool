from django.contrib import admin
from main.models import SiteSetting

# Register your models here.
# class SiteSettingAdmin(admin.ModelAdmin):
#     list_display = ['']

admin.site.register(SiteSetting)
