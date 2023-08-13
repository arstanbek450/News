from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def homepage(request):
    context = {}
    context["name"] = "Kaium"
    posts_list = Post.objects.all() # SELECT * FROM Post;
    context["posts"] = posts_list
    return render(request, "home.html", context)
def post_detail(request, id):
    context = {}
    post_object = Post.objects.get(id=id)
    context["post"] = post_object
    return render(request, "post_info.html", context)
def profile_detail(request, id):
    context = {}
    context['profile'] = Profile.objects.get(id=id)
    return render(request, 'profiple_detail.html', context)


def shorts(request):
    context = {
        'short_info': Short.objects.all()
    }
    return render(request, "shorts.html", context)

def short_info(request, id):
    context = {"short": Short.objects.get(id=id)}
    return render(request, "short_info.html", context)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'category_detail.html', {'category': category})


def contacts(request):
    return HttpResponse("Наши контакты!")

def about_us(request):
    return HttpResponse("Информация о нас!")



