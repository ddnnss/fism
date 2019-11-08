from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html', locals())
def index1(request):
    return render(request, 'index1.html', locals())
def lk(request):
    return render(request, 'lk.html', locals())
def search(request):
    allcat = Category.objects.all()
    allfil = Filter.objects.all()
    return render(request, 'search.html', locals())
