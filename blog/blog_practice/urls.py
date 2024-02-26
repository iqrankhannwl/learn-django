from django.urls import path
from .views import home, create_blog, detail, delete_blog
urlpatterns=[
    path("", home, name="home"),
    path("create/", create_blog, name="create_blog" ),
    path("blog/<int:id>/", detail,  name="detail"),
    path("delete_blog/<int:id>/", delete_blog,  name="delete"),


]