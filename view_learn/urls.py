from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('home/', home, name = "home"),
    # path('author/<int:author_id>/', author, name = "author"),
    # re_path(r'author/(?P<author_id>[0-9]+)/?', author, name = "author"),
    re_path(r'author/(?P<author_id>[0-9]+)/?', author, name = "author"),
    path('author_name/<n>/', author_name, name = "author_name"),
    # re_path(r'home/?', home, name = "home")
]