from django.urls import path

from zoomit_savelist.views import save_post, saved_list, delete_saved

urlpatterns = [
    path('save-post', save_post),
    path('saved-list', saved_list),
    path('delete-saved', delete_saved),
]
