from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User
#from django.urls import reverse


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    image = models.ImageField()                          
    body = models.TextField()
    published = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-published',)
        
    def __str__(self):
        return self.title


    

#create model for Email
class Email(models.Model):
    '''Creating the email table in my database'''
    field_name = models.EmailField(max_length=254)



