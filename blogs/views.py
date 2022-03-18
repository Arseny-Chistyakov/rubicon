from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from blogs.models import Post


def index(request):
    context = {'title': 'Рубикон'}
    return render(request, 'blogs/index.html', context=context)


def blogs(request, page=1):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    try:
        posts_paginator = paginator.page(page)
    except PageNotAnInteger:
        posts_paginator = paginator.page(1)
    except EmptyPage:
        posts_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': 'Рубикон - Блог',
        'posts': posts_paginator,
    }
    return render(request, 'blogs/blogs.html', context=context)
