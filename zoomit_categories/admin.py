from django.contrib import admin

# Register your models here.
from zoomit_categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'slug']


admin.site.register(Category, CategoryAdmin)
