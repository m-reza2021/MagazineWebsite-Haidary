from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from zoomit_accounts.models import ProfileImage
from zoomit_comments.foms import UserCommentForm, UserCommentReplyForm
from zoomit_comments.models import UserComment, UserCommentReply
from zoomit_posts.models import Post


@login_required(login_url='/login')
def post_comment(request):
    user_comment_form = UserCommentForm(request.POST or None)

    user_image_path: ProfileImage = ProfileImage.objects.filter(user_id=request.user.id).first()
    user_image = user_image_path.image

    if user_comment_form.is_valid():
        post_id = user_comment_form.cleaned_data.get('post')
        body = user_comment_form.cleaned_data.get('body')

        comment = UserComment.objects.create(user_id=request.user.id, post_id=post_id, body=body, user_image=user_image)
        if comment:
            post = Post.objects.get(id=post_id)
            return redirect(post.get_absolute_url())


@login_required(login_url='/login')
def comment_reply(request):
    comment_reply_form = UserCommentReplyForm(request.POST or None)

    user_image_path: ProfileImage = ProfileImage.objects.filter(user_id=request.user.id).first()
    user_image = user_image_path.image

    if comment_reply_form.is_valid():
        post_id = request.POST.get('post_id')
        comment_id = request.POST.get('comment_id')
        body = comment_reply_form.cleaned_data.get('body')

        reply: UserCommentReply = UserCommentReply.objects.create(user_id=request.user.id, comment_id=comment_id,
                                                                  body=body, user_image=user_image)
        post = Post.objects.get(id=post_id)
        if reply:
            print(reply)
            return redirect(post.get_absolute_url())