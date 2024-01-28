from django.db import models
from registration.models import CustomUser

class BookList(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_isbn = models.CharField(max_length=13)
    book_title = models.CharField(max_length=255)
    book_creator = models.CharField(max_length=255)
    book_publisher = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field="user_id")
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['book_isbn','user'], name='unique_book')
        ]