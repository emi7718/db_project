#from django.shortcuts import render  <<< this was here when I opened views.py for the 1st time
# Create your views here.


from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World. You\'re at the polls index')
    