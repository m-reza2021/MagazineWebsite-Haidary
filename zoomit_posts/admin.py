from django.contrib import admin

# Register your models here.
from zoomit_posts.models import Post
from .forms import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'issue_date', 'views']
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
