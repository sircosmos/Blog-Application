from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('email', views.home, name='email'),
    path('edit', views.edit, name='edit'),
    path('content', views.content, name='content'),
    path('sign', views.sign, name='sign'),
    path('log', views.log, name='log'),
    path('add_newsletter', views.add_newsletter, name='newsletter'),
]