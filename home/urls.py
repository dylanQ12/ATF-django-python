from django.urls import path
from .views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("section/about/", about_view, name="about"),
    path("section/services/", services_view, name="services-section"),
    path("section/detail-service/<uuid:pk>/", detail_service, name="detail-service"),
    path("section/blog/", blog_view, name="blog"),
    path("section/detail-blog/<uuid:pk>/", blog_detail, name="detail-blog"),
    path("section/team/", team_view, name="team"),
    path("section/contact/", contact_view, name="contact"),
]