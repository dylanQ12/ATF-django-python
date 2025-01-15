from django.shortcuts import get_object_or_404, render
from services.models import Service
from blog.models import Post


def home_view(request):
    context = {
        "title": "inicio"
    }
    return render(request, "home.html", context)


def about_view(request):
    context = {"title": "Nosotros"}
    return render(request, "pages/about.html", context)


def services_view(request):
    services = Service.objects.only(
        "uuid",
        "name", 
        "description", 
        "image", 
        "date_created"
    ).order_by("-date_created")
    
    context = {
        "title": "Servicios",
        "services": services,
    }
    
    return render(request, "pages/service.html", context)


def detail_service(request, pk):
    service = get_object_or_404(Service, uuid=pk) 
    context = {
        "title": service.name,
        "service": service
    }
    return render(request, "pages/details/service-detail.html", context)


def blog_view(request):
    posts = Post.objects.only(
        "image",
        "title",
        "date_created",
        "author",
        "description"
    ).order_by("-date_created")
    
    context = {
        "title": "Blog",
        "posts": posts
    }
    return render(request, "pages/blog.html", context)


def blog_detail(request, pk):
    post = get_object_or_404(Post, uuid=pk)  # Buscar usando el campo 'uuid'
    context = {
        "title": post.title,
        "post": post
    }
    return render(request, "pages/details/blog-detail.html", context)


def team_view(request):
    context = {"title": "Equipo"}
    return render(request, "pages/team.html", context)


def contact_view(request):
    services = Service.objects.only(
        "name"
    ).order_by("-date_created")
    
    context = {
        "title": "Contáctanos",
        "services": services
    }
    return render(request, "pages/contact.html", context)
