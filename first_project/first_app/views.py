from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    dict = {'value':'See you!'}
    return render(request,'first_app/home.html',context =dict)