from django.contrib import admin

# Register your models here.
from zoomit_ads.models import Advertise


class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'link']


admin.site.register(Advertise, AdvertiseAdmin)