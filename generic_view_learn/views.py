from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView

from .models import *

# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, 'generic_view_learn/index.html', {})
    
    def post(self, request):
        return HttpResponse('Hello Postman !')

class HomePage(TemplateView):
    template_name = 'generic_view_learn/homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'Name' : 'Jatin Katyal'
        }

        return context

# All query set
class AuthorList(ListView):
    template_name = 'generic_view_learn/author_list.html'
    model = Author
# def author_list(request):
#     if request.method == "GET":
#         authors = Author.object.all()

#         context = {
#             'object_list' : authors
#         }

#         return render(request, '', context)

# Static Query set
class TopAuthorsList(ListView):
    template_name = 'generic_view_learn/top_author_list.html'
    context_object_name = 'top_authors'
    queryset = Author.objects.filter(score__gt = 3).order_by('-score')

    def get_context_data(self):
        context = super().get_context_data()

        context['admin_name'] = "Jatin"

        return context

# Dynamic Query Set
class TopAuthorsListByGet(ListView):
    template_name = 'generic_view_learn/top_author_list.html'
    context_object_name = 'top_authors'

    def get_queryset(self):
        min_rating = int(self.request.GET['rating'])

        return Author.objects.filter(score__gt = min_rating)


# Detail View
class Author(DetailView):
    template_name = 'generic_view_learn/author_detail.html'
    context_object_name = 'author'
    model = Author

class Book(DetailView):
    template_name = 'generic_view_learn/book_detail.html'
    context_object_name = 'book'
    model = Book