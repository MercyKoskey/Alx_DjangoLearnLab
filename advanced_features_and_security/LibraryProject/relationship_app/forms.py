from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # or list fields explicitly, e.g. ['title', 'author', 'publication_year']
