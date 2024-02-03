from django.shortcuts import render
from django.http import request , HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='login')
def library(request):
    return render(request , 'library.html')