from django.urls import path

from zoomit_posts.views import (single_post, PostList, PostListByCategory,
                                posts_sidebar, PostListSearch, PostListByTag,)

urlpatterns = [
    path('posts', PostList.as_view(), name='posts'),
    path('posts/search', PostListSearch.as_view(), name='search'),
    path('post/<post_id>/<post_title>', single_post),
    path('posts/category/<category_name>', PostListByCategory.as_view()),
    path('posts/tag/<tag_name>', PostListByTag.as_view()),
    path('posts-sidebar', posts_sidebar, name='posts_sidebar'),
]