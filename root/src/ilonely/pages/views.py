from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from pages.models import Follow
from pages.models import Profile

# Create your views here.

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pages/home.html',
        {
            'title':'Home',
        }
    )

def register(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pages/register.html',
        {
            'title':'Registration',
        }
    )

def login(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pages/login.html',
        {
            'title':'Login',
        }
    )

def forgot_username(request):
    return render(
        request,
        'pages/forgot_username.html',
        {
            'title':'Forgot Username',
        }
    )

def forgot_password(request):
    return render(
        request,
        'pages/forgot_password.html',
        {
            'title':'Forgot Password',
        }
    )

def view_following(request):
    myid = request.user.id
    followset = Follow.objects.filter(userFollowing=myid)
    usersIFollow = Profile.objects.Filter(user = followset.user)
    return render(request, 'pages/view_following.html', 
                  { 'title':'Following', 
                   'following' : usersIFollow,} 
                  )