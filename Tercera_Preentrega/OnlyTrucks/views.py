from django.shortcuts import render
from OnlyTrucks.models import Post

def index(request):
    return render(request, "OnlyTrucks/index.html")

def Camiones(request):
    
    posts = Post.objects.all()
    return render(request, "OnlyTrucks/Camiones.html",{"posts": posts})