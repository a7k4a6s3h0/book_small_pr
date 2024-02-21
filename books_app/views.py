from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from . models import *
from .dj_forms import *

# Create your views here.


def list_view(request):
    books_list = Books.objects.all().order_by('?')
    return render(request, 'book_list.html', {'obj_list': books_list})

def add_books_views(request):
    if request.method == 'POST':
        
        form = BooksForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('/')  
        else:

            messages.error(request, "An error occurred while adding the book. Please try again.")
            return redirect('add_book') 
        
    return render(request, 'add.html')

def update_view(request, slug):
    book_instance = get_object_or_404(Books, slug=slug)

    if request.method == 'POST':
        form = UpdateBooksForm(request.POST, request.FILES, instance=book_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect('/') 

    else:
        form = UpdateBooksForm(instance=book_instance)

    return render(request, 'update.html', {'instance': book_instance})

def delete_view(request, slug):
    book_instance = get_object_or_404(Books, slug=slug)
    book_instance.delete()
    messages.success(request,"book sucessfully deleted...!!")
    return redirect('/')
