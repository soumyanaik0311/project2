from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def telugu(request):
    return HttpResponse("this is our telugu movies function")
