from django.shortcuts import render
from OnlyTrucks.models import Post
from OnlyTrucks.forms import PostForm

def index(request):
    return render(request, "OnlyTrucks/index.html")

def Camiones(request):
    
    posts = Post.objects.all()
    return render(request, "OnlyTrucks/Camiones.html",{"posts": posts})

def mostrar_post(request):
    
    context = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }
    
    return render(request, "OnlyTrucks/admin_post.html", context )

def agregar_post(request):
    post_form = PostForm(request.POST)
    post_form.save()
    context = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }
    
    return render(request, "OnlyTrucks/admin_post.html", context)

def buscar_post(request):
    criterio= request.GET.get("criterio")
    context = {
        "posts":Post.objects.filter(Modelo_de_su_Camion__icontains=criterio).all(),
    }
    
    return render(request, "OnlyTrucks/Camiones.html", context)