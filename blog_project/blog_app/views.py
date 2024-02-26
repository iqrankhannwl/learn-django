from django.shortcuts import render, redirect
from .models import Blogs
# Create your views here.


def home(request):
    blogs = Blogs.objects.all()
    return render(request, "index.html", {"blogs":blogs})

def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        tags = request.POST.get("tags")
        description = request.POST.get("description")
        blog = Blogs(title=title, author=author, tags =tags, description=description)
        blog.save()
        return redirect("/")

    return render(request, "create.html")

def detail(request, id):
    blog = Blogs.objects.get(pk=id)
    return render(request, "detail.html", {"blog":blog})

def delete_blog(request, id):
    blog =  Blogs.objects.get(pk=id)
    blog.delete()
    return redirect("/")