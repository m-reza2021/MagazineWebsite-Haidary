import random

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib import messages

# Create your views here.
from zoomit_accounts.forms import LoginForm, RegisterForm, ProfilePictureForm, UpdateProfileForm
from zoomit_accounts.models import ProfileImage
from zoomit_comments.models import UserComment, UserCommentReply
from zoomit_media.models import RandomImage

User = get_user_model()


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        username = login_form.cleaned_data.get('username').lower()
        password = login_form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('username', 'کاربری با مشخصات وارد شده یافت نشد')

    context = {
        'login_form': login_form
    }
    return render(request, 'accounts/login_page.html', context)


def signup_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        email = register_form.cleaned_data.get('email').lower()
        username = register_form.cleaned_data.get('username').lower()
        password = register_form.cleaned_data.get('password')

        new_user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                            email=email, username=username, password=password)
        if new_user:
            index = random.randint(1, 7)
            image = f'/static/images/profile/{index}.png'

            ProfileImage.objects.create(user_id=new_user.id, image=image)
            messages.success(request, 'ثبت نام شما با موفقیت انجام شد.')
            return redirect('/login')

    context = {
        'register_form': register_form
    }
    return render(request, 'accounts/signup_page.html', context)


def logout_route(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def profile(request):
    image_form = ProfilePictureForm(request.POST or None, request.FILES)
    profile_update_form = UpdateProfileForm(request.POST or None,
                                            initial={'first_name': request.user.first_name,
                                                     'last_name': request.user.last_name,
                                                     'username': request.user.username,
                                                     'email': request.user.email})

    profile: ProfileImage = ProfileImage.objects.filter(user_id=request.user.id).last()
    comments = UserComment.objects.filter(user_id=request.user.id)
    replies = UserCommentReply.objects.filter(user_id=request.user.id)

    if profile is not None:
        for x in comments:
            x.user_image = profile.image
            x.save()

        for x in replies:
            x.user_image = profile.image
            x.save()

    context = {
        'page_title': profile.user,
        'image': profile,
        'image_form': image_form,
        'profile_form': profile_update_form,
    }

    return render(request, 'accounts/profile.html', context)


@login_required(login_url='/login')
def image_upload(request):
    image_form = ProfilePictureForm(request.POST or None, request.FILES)
    profile: ProfileImage = ProfileImage.objects.filter(user_id=request.user.id).last()

    if image_form.is_valid():
        image = image_form.files.get('image')
        if profile:
            profile.image = image
            profile.save()
        else:
            uploded = ProfileImage.objects.create(user_id=request.user.id, image=image)
            if uploded:
                # comments = UserComment.objects.filter(user_id=request.user.id)
                # for x in comments:
                #     x.user_image = profile.image.url
                #     x.save()
                print(uploded)
                print('done!')
                return redirect('/profile')
            else:
                raise Http404('something wrong')

    return redirect('/profile')


@login_required(login_url='/login')
def profile_update(request):
    profile_update_form = UpdateProfileForm(request.POST or None)

    if profile_update_form.is_valid():
        first_name = profile_update_form.cleaned_data.get('first_name')
        last_name = profile_update_form.cleaned_data.get('last_name')
        username = profile_update_form.cleaned_data.get('username').lower()
        email = profile_update_form.cleaned_data.get('email').lower()
        user = User.objects.filter(id=request.user.id).first()

        user.first_name = first_name
        user.last_name = last_name
        if user.username == username:
            pass
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'نام کاربری قبلا ثبت شده است')
        else:
            user.username = username

        if user.email == email:
            pass
        elif '.comm' in email or '.nett' in email:
            messages.error(request, 'ایمیل وارد شده معتبر نمیباشد')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'ایمیل قبلا ثبت شده است')
        else:
            user.email = email
        user.save()
        return redirect('/profile')

    return redirect('/profile')