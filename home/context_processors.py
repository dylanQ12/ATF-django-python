from .models import Carrusel
from services.models import Service
from blog.models import Post
from datetime import datetime


def get_latest_list(request):
    # All latest 5 carrusels.
    latest_carrusel = Carrusel.objects.only(
        "image",
        "title",
        "description",
    ).order_by("-date_created")[:5]
    
    
    # Latest 4 Services created.
    latest_services = Service.objects.only(
        "name", 
        "description", 
        "image", 
        "date_created"
    ).order_by("-date_created")[:4]
    

    # Lastest 3 Posts created
    latest_posts = Post.objects.only(
        "image",
        "title",
        "date_created",
        "author",
        "description"
    ).order_by("-date_created")[:3]
    
    
    # Lastest 2 Posts created
    latest_post = Post.objects.only(
        "title",
        "description"
    ).order_by("-date_created")[:2]
    
    
    data = {
        "current_year": datetime.now().year,
       "latest_carrusel": latest_carrusel,
       "latest_services": latest_services,
       "latest_posts": latest_posts,
       "latest_post": latest_post
    }
    
    return data
    
