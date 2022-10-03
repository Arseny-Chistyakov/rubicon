from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from blogs.forms import CommentForm
from blogs.models import Post, Comment


def index(request):
    return render(request, 'blogs/index.html', context={'title': 'Рубикон'})


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
        'title': 'Блог',
        'posts': posts_paginator,
    }
    return render(request, 'blogs/blogs.html', context=context)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, status='published', slug=post_slug)
    comments = Comment.objects.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(request.path)
    else:
        comment_form = CommentForm()
    context = {
        'title': 'Подробнее о посте',
        'post': post,
        'comments': comments,
        'comment_form': comment_form}
    return render(request, 'blogs/post_detail.html', context=context)
