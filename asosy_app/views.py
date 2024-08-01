from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    categorya = Category.objects.all()
    return render(request, 'index.html', context={'categorya':categorya})

def post(request, c_id):
    categorya = Category.objects.get(id=c_id)
    post = Post.objects.filter(category=categorya)
    return render(request, 'post.html', context={'posts':post}) 

