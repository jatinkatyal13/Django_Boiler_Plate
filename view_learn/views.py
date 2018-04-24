from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.

def author_name(request, n):

    author = get_object_or_404(Author, name__startswith = n)
    # author = Author.objects.get(name__startswith = n)

    context = {
        'author' : author
    }

    return render(request, 'author.html', context)

def author(request, author_id):

    author = get_object_or_404(Author, pk = author_id)

    context = {
        'author' : author
    }

    return render(request, 'author.html', context)


@login_required
def home(request):

    if request.method == "GET":

        min_rating = int(request.GET['rating'])

        books = Book.objects.filter(rating__gte = min_rating)

        # i = request.GET['id']

        # author = get_object_or_404(Author, pk = i)

        # try:
        #     author = Author.objects.get(pk = i)
        # except:
        #     raise Http404()

        # c = {
        #     'author' : author
        # }

        c = {
            'books' : books
        }

        return render(request, 'index.html', c)

    elif request.method == "POST":
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        c = {
            'first' : first_name,
            'last' : last_name
        }

        return render(request, 'index.html', c)
        