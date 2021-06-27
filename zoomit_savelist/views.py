from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from zoomit_posts.models import Post
from zoomit_savelist.models import SaveList


@login_required(login_url='/login')
def save_post(request):
    post_id = request.POST.get('post_id')

    saved_item = SaveList.objects.create(owner_id=request.user.id, post_id=post_id)
    if saved_item:
        post = Post.objects.get_product_by_id(post_id)
        return redirect(post.get_absolute_url())


@login_required(login_url='/login')
def saved_list(request):
    saved_posts: SaveList = SaveList.objects.filter(owner_id=request.user.id)
    context = {
        'saved': saved_posts
    }
    return render(request, 'saved/saved_list.html', context)


@login_required(login_url='/login')
def delete_saved(request):
    if request.POST:
        saved_id = request.POST.get('save_id')

        saved_post: SaveList = SaveList.objects.get(owner_id=request.user.id, id=saved_id)
        if saved_post:
            saved_post.delete()
            messages.success(request, 'پست از لیست حذف شد.')
            return redirect('/saved-list')