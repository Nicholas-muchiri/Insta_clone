from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Image, Profile
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login/')
def insta(request):
    post = Image.objects.all()
    return render(request,'insta.html',{"post":post})

def pics(request):
    pictures = Image.objects.all()

    return render(request, "insta.html", {"pictures": pictures})

# @login_required(login_url='/accounts/login/')
# def insta(request, article_id):

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})


def profile(request, username):
    profile = User.objects.get(username=username)
    # print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile.username} Instagram photos and videos'

    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'images':images})
