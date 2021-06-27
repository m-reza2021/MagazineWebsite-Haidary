from django.contrib import admin

# Register your models here.
from zoomit_posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'issue_date', 'views']


admin.site.register(Post, PostAdmin)
