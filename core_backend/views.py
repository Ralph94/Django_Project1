from django.shortcuts import render
from django.views.generic import DeleteView
from .models import Post
posts = (
    {
        'author':'Rafael P',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'9/29/2020'
    },
    {
        'author': 'Rafael P',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '9/30/2020'
    }
)
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'core_backend/home.html', context)

def about(request):
    return render(request,'core_backend/about.html')






