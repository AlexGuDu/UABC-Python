from django.shortcuts import render
from django.http import HttpResponse
from . models import Posts
from .forms import FormCreate

# Create your views here.
def index(request):
    # return HttpResponse('HELLO FROM POSTS')

    posts = Posts.objects.all()
    context = {
        'title': 'Latest posts',
        'posts': posts
    }

    return render(request, 'posts/index.html', context)

    # return render(request, 'posts/index.html', {
    # 'title': 'Latest posts'
    # })

def details(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)


def create(request):
    form = FormCreate(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
    else:
        form = FormCreate(request.POST or None)
    context = {
        "form": form
    }
    return render(request, "posts/create.html", context)
