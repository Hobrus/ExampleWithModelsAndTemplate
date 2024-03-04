from django.shortcuts import render
from django.http import HttpResponse

from app1.models import Post


# Create your views here.
def HelloWorld(request):
    return HttpResponse("Hello")


def main_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "1.html", context=context)
