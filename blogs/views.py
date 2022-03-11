from django.shortcuts import render

from blogs.models import New


def index(request):
    context = {'title': 'Рубикон'}
    return render(request, 'blogs/index.html', context=context)


def blogs(request):
    context = {
        'title': 'Рубикон - Блог',
        'news': New.objects.all(),
    }
    return render(request, 'blogs/blogs.html', context=context)
