from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name = "index"),
    path('home/', HomePage.as_view(), name = "home"),
    path('authors/', AuthorList.as_view(), name = "authors"),
    path('top_authors/', TopAuthorsList.as_view(), name = "top_authors"),
    path('top_authors_by_get/', TopAuthorsListByGet.as_view(), name = "top_authors_get"),
    path('author/<int:pk>', Author.as_view(), name = "author"),
    path('book/<slug:slug>', Book.as_view(), name = "book"),
]