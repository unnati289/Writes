from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    title=models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description=models.TextField(default="Nothing yet")

    def __str__(self):
        return self.title
class WriteUp(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='writeups')
    content=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.book.title}'
    
# Create your models here.
