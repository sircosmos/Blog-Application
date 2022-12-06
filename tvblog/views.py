from django.shortcuts import render, redirect
from .models import Post



# Create your views here.
def home(request):
    '''renders home page when the user is logged in'''
    my_post = Post.objects.all()
    return render(request, 'index.html', {'post':my_post})


def profile(request):
    '''renders the profile page when the user is logged in'''
    return render(request, 'profile.html')

def content(request):
    '''renders index page when the user is logged in'''
    return render(request, 'content.html')

def email(request):
    '''renders email page when the user is logged in'''
    return render(request, 'email.html')

def edit(request):
    '''renders edit page when the user is logged in'''
    return render(request, 'edit.html')

def sign(request):
    '''renders sign page when the user is logged in'''
    return render(request, 'sign.html')

def log(request):
    '''renders sign page when the user is logged in'''
    return render(request, 'log.html')

#def add_newsletter(request):
    #'''add email to the database'''
    #newsletter_passed = request.POST.get('newsletter')
    #print(newsletter_passed)
    #return redirect('home')


def add_newsletter(request):
    if request.method == 'POST':
        newsletter_passed = request.POST.get('newsletter')
        if newsletter_passed:
            new_newsletter = newsletter_passed()
            new_newsletter.name = newsletter_passed
            new_newsletter.save()
    return redirect('home')



