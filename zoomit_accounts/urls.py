from django.urls import path

from zoomit_accounts.views import login_page, signup_page, logout_route, profile, image_upload, profile_update

urlpatterns = [
    path('login', login_page),
    path('signup', signup_page),
    path('logout', logout_route),
    path('profile', profile),
    path('image-upload', image_upload),
    path('profile_update', profile_update),
]