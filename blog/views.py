from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from datetime import date
from .models import Post, Author, Tag

# Create your views here.

def starting_page(request):
    """
    
    """
    posts = Post.objects.all().order_by('-date')[:3] # Només els 3 més recents
    return render(request, "blog/index.html", {"posts": posts})

def posts(request):
    """
    Vista para mostrar todos los posts del blog.
    """
    all_posts = Post.objects.all().order_by('-date')
    return render(request, "blog/post_list.html", {"all_posts": all_posts})

def post_detail(request, slug):
    """
    Vista para mostrar los detalles de un post específico.
    """
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})

def autors(request):
    """
    Vista para mostrar los autores
    """
    authors = Author.objects.all()
    return render(request, "blog/authors_list.html", {"authors": authors})

def autors_detail(request, slug):
    """
    
    """
    author = get_object_or_404(Author, last_name__iexact=slug)
    posts = Post.objects.filter(author=author).order_by("-date")
    return render(request, "blog/author_detail.html", {
        "author": author,
        "posts": posts
    })

def tags_page(request):
    """
    
    """
    tags = Tag.objects.all()
    return render(request, "blog/tags_list.html", {"tags": tags})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, tag__iexact=slug)
    posts = Post.objects.filter(tags=tag).order_by("-date")

    return render(request, "blog/tag_detail.html", {
        "tag": tag,
        "posts": posts
    })


