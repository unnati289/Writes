from django.urls import path
from .views import add_book, add_writeup,BookListView,book_detail_view,writeup_detail

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),  # Assuming you have a view for listing books
    path('book/add/', add_book, name='add-book'),  # URL for adding a new book
    path('book/<int:book_id>/add-writeup/', add_writeup, name='add-writeup'),  # URL for adding write-up for a specific book
    path('<int:book_id>/', book_detail_view, name='book-detail'),
    path('writeups/<int:writeup_id>/', writeup_detail, name='writeup-detail'),
]
