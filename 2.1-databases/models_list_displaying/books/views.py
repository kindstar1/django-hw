from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'

    book_objects = Book.objects.all()
    sort = request.GET.get('sort')
    
    books = [obj for obj in book_objects]
    context = {
        'books': books,
        }
    return render(request, template, context)

def date_pub_view(request, publish):
    template = 'books/books_publish.html'

    current_date_obj = Book.objects.filter(pub_date=publish)
    previous_date_obj = Book.objects.filter(pub_date__lt=publish).order_by('-pub_date').first()
    next_date_obj = Book.objects.filter(pub_date__gt=publish).order_by('pub_date').first()
    
    context = {
        'books': current_date_obj,
        'previous_book': previous_date_obj,
        'next_book': next_date_obj,
        }
    return render(request, template, context)

