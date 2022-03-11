from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blogs.models import New


def index(request):
    context = {'title': 'Рубикон'}
    return render(request, 'blogs/index.html', context=context)


def blogs(request, page=1):
    news = New.objects.all()
    paginator = Paginator(news, 2)
    try:
        news_paginator = paginator.page(page)
    except PageNotAnInteger:
        news_paginator = paginator.page(1)
    except EmptyPage:
        news_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': 'Рубикон - Блог',
        'news': news_paginator,
    }
    return render(request, 'blogs/blogs.html', context=context)
