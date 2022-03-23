from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='uploaded_picture',blank=True,null=True)
    author=models.CharField(max_length=100)
    publish_date=models.DateField(blank=True,null=True)   
    borrow_start_date=models.DateField(blank=True,null=True)
    borrow_end_date=models.DateField(blank=True,null=True)
    
    def __str__(self):
        return self.book_name