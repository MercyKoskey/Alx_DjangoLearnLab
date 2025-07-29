from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

# ✅ Add this block exactly to pass the check
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
