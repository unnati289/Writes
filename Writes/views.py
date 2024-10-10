from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, WriteUp, User
from .forms import BookForm, WriteUpForm
from django.views.generic import ListView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
# Create your views here.
def superuser_required(user):
    
    return user.is_superuser
@user_passes_test(superuser_required,login_url='book-list')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()

    return render(request, 'Writes/add_book.html', {'form': form})
@user_passes_test(superuser_required,login_url='book-list')
def add_writeup(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = WriteUpForm(request.POST)
        if form.is_valid():
            writeup = form.save(commit=False)
            writeup.book = book
            writeup.save()
            #notify_users_of_new_writeup(writeup)
            return redirect('book-detail', book_id=book.id)
    else:
        form = WriteUpForm()  # Initialize the form for GET requests

    return render(request, 'Writes/add_writeup.html', {'form': form, 'book': book})

def notify_users_of_new_writeup(writeup):
    users = User.objects.all()
    for user in users:
        send_mail(
            subject=f'New Write-Up on "{writeup.book.title}"',
            message=f'A new write-up has been added. Check it out!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
class BookListView(ListView):
    model = Book
    template_name = 'Writes/list.html'  # Specify your template name
    context_object_name = 'books'

def book_detail_view(request, book_id):
    # Retrieve the book or return a 404 error if not found
    book = get_object_or_404(Book, id=book_id)
    
    # Render the detail.html template with the book context
    return render(request, 'Writes/detail.html', {'book': book})

def writeup_detail(request, writeup_id):
    # Retrieve the write-up by its ID or return a 404 error if not found
    writeup = get_object_or_404(WriteUp, id=writeup_id)
    
    # Render the write-up detail template with the write-up context
    return render(request, 'Writes/writeup-detail.html', {'writeup': writeup})