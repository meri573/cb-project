from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return render(request, 'point_site/index.html')


def loginView(request):
    pass