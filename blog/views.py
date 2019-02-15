from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')


def post_list(request):
    return render(request, 'blog/post_list.html', {'posts': posts})
