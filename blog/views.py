from django.shortcuts import render
from . import models
from django.utils import timezone


def post_list(request):
    posts = models.Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
