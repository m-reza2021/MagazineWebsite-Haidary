from django.contrib import admin

# Register your models here.
from zoomit_tags.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'slug']


admin.site.register(Tag, TagAdmin)
