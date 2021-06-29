import random
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from zoomit_ads.models import Advertise
from zoomit_categories.models import Category
from zoomit_comments.models import UserComment
from zoomit_posts.models import Post


def home_page(request):
    posts = Post.objects.all().order_by('-id')
    for post in posts:
        index = random.randint(1,9)
        post.image = f'/static/images/posts/{index}.png'
        post.save()

    main_posts = Post.objects.all().order_by('-id')

    paginator = Paginator(main_posts, 10)
    page = request.GET.get('page')

    try:
        main_posts = paginator.page(page)
    except PageNotAnInteger:
        main_posts = paginator.page(1)
    except EmptyPage:
        main_posts = paginator.page(paginator.num_pages)

    ads = Advertise.objects.all().order_by('-id')
    for ad in ads:
        index = random.randint(1,9)
        ad.image = f'static/images/posts/{index}.png'
        ad.save()

    context = {
        'page_title': 'خانه',
        'posts': posts,
        'main_posts': main_posts,
        'pages': main_posts,
        'ads': ads,
    }
    return render(request, 'home_page.html', context)


def categories(request):
    category = Category.objects.all()
    context = {
        'categories': category
    }
    return render(request, 'shared/Header.html', context)


def footer(request):
    posts = Post.objects.all().order_by('-views')
    context = {
        'comments': UserComment.objects.all(),
        'posts': posts
    }
    return render(request, 'shared/Footer.html', context)
