from django.urls import path

from zoomit_comments.views import post_comment, comment_reply

urlpatterns = [
    path('post-comment', post_comment),
    path('comment-reply', comment_reply),
]