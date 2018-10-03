from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Image

# Create your views here.
def insta(request):
    return render(request, 'insta.html')


def pics(request):
    pictures = Image.objects.all()

    return render(request, "insta.html", {"pictures": pictures})

# @login_required(login_url='/accounts/login/')
# def insta(request, article_id):