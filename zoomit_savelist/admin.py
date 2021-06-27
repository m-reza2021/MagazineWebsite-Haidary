from django.contrib import admin

# Register your models here.
from zoomit_savelist.models import SaveList


class SaveListAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'owner']


admin.site.register(SaveList, SaveListAdmin)
