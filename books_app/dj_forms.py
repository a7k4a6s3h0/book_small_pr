from django import forms
from . models import *
class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_name', 'book_describtion', 'book_img']

class UpdateBooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_name', 'book_describtion', 'book_img']        