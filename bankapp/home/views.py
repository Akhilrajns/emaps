from django.shortcuts import render
from django.template import RequestContext
 
def home(request):
    return render(request, 'home/index.html', {'title':'Home Page',})


def mobile(request):
    return render(request, 'home/mobile.html', {'title':'Home Page',})    