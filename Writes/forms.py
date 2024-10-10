from django import forms
from .models import Book,WriteUp
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

class WriteUpForm(forms.ModelForm):
    class Meta:
        model=WriteUp
        fields=['content']