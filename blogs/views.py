from django.shortcuts import render


def index(request):
    context = {'title': 'Рубикон'}
    return render(request, 'blogs/index.html', context=context)


def blogs(request):
    context = {'title': 'Рубикон'}
    return render(request, 'blogs/blogs.html', context=context)
