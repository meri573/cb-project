from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def homePageView(request):
    return render(request, 'point_site/index.html')


def loginView(request):
    pass