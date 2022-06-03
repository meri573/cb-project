from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from.models import Points
from django.contrib.auth.models import User

# Create your views here.

@login_required
def homePageView(request):
    try:
        pojot = Points.objects.get(owner=request.user)
    except:
        p = Points(owner=request.user)
        p.save()
        pojot = Points.objects.get(owner=request.user)

    users = User.objects.exclude(pk=request.user.id)

    return render(request, 'point_site/index.html',{'points': pojot, 'users': users})

