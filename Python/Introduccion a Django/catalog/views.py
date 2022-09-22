from telnetlib import STATUS
from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    num_boks = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.all().count()

    disponibles = BookInstance.objects.filter(status__exact = 'a').count()
    return render(request, "index.html", context={"num_books":num_boks,
                            "num_authors":num_authors,
                            "disponibles":disponibles,
                            "num_instances":num_instances
    }
    )
