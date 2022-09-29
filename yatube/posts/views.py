from .models import Post, Group
from django.shortcuts import get_object_or_404, render

COUNT_POST = 10


def index(request):
    posts = Post.objects.all().order_by('-pub_date')[:COUNT_POST]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


COUNT_GROUP_POSTS = 10


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all().order_by('-pub_date')[:COUNT_GROUP_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
