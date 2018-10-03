from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404

# Create your views here.
def insta(request):
    return render(request, 'insta.html')