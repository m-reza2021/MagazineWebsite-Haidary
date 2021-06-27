from django.contrib import admin

# Register your models here.
from zoomit_comments.models import UserComment, UserCommentReply

admin.site.register(UserComment)
admin.site.register(UserCommentReply)