from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
from zoomit_accounts.models import ProfileImage
from zoomit_categories.models import Category
from zoomit_comments.foms import UserCommentForm, UserCommentReplyForm
from zoomit_comments.models import UserComment
from zoomit_counter.models import ViewCounter
from zoomit_posts.models import Post
from zoomit_savelist.models import SaveList


class PostList(ListView):
    template_name = 'posts/posts_list.html'
    paginate_by = 6

    def get_queryset(self):
        posts = Post.objects.all().order_by('-id')
        return posts

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context['page_title'] = 'همه مطالب'
        return context


def single_post(request, *args, **kwargs):
    post_id = kwargs['post_id']
    post = Post.objects.get_product_by_id(post_id)

    # post view counter user base
    if request.user.is_authenticated:
        post_counter = ViewCounter.objects.filter(user_id=request.user.id, post_id=post_id)
        if not post_counter:
            ViewCounter.objects.create(user_id=request.user.id, post_id=post_id)

        count = ViewCounter.objects.filter(post_id=post_id).count()

        update_post: Post = Post.objects.get(id=post_id)
        if update_post:
            update_post.views = count
            update_post.save()

    related_post = Post.objects.get_posts_by_category(post.category.slug)\
        .order_by('-id').exclude(id=post_id)

    # check if a post saved by user
    saved = SaveList.objects.filter(owner_id=request.user.id, post_id=post_id).first()

    # image of post's author
    author = ProfileImage.objects.get(user_id=post.author.id)

    # comment & reply forms
    user_comment_form = UserCommentForm(request.POST or None, initial={'post': post_id})
    comment_reply_form = UserCommentReplyForm(request.POST or None)

    comments: UserComment = UserComment.objects.filter(post_id=post_id)

    context = {
        'page_title': post.title,
        'post': post,
        'author': author,
        'related_posts': related_post,
        'saved': saved,
        'post_comment_form': user_comment_form,
        'comment_reply_form': comment_reply_form,
        'comments': comments,
        'latest_posts': Post.objects.all().order_by('-id').exclude(id=post_id),
    }
    return render(request, 'posts/single_post.html', context)


class PostListByCategory(ListView):
    template_name = 'posts/posts_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        posts = Post.objects.get_posts_by_category(category_name)
        return posts

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(PostListByCategory, self).get_context_data(*args, **kwargs)
        category_name = self.kwargs['category_name']
        category = Category.objects.get(slug=category_name)
        context['category_name'] = f'دسته: {category}'
        context['page_title'] = category
        return context


class PostListByTag(ListView):
    template_name = 'posts/posts_list.html'
    paginate_by = 6

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        posts = Post.objects.get_posts_by_tag(tag_name)
        return posts

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(PostListByTag, self).get_context_data(*args, **kwargs)
        tag_name = self.kwargs['tag_name']
        context['tag_name'] = f'برچسب: {tag_name}'
        context['page_title'] = tag_name
        return context


class PostListSearch(ListView):
    template_name = 'posts/posts_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        return Post.objects.search_posts(query)


def posts_sidebar(request):
    posts = Post.objects.all().order_by('-views')
    return render(request, 'posts/shared/posts_sidebar.html', {'posts': posts})