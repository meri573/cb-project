from django.shortcuts import render, redirect
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

@login_required
def sendView(request):

    receiver = User.objects.get(username=request.POST.get('to'))
    receiver = Points.objects.get(owner=receiver)
    sender = Points.objects.get(owner=request.user)
    amount = int(request.POST.get('amount'))

    sender.points = sender.points - amount
    receiver.points = receiver.points + amount
    sender.save()
    receiver.save()
    return redirect('/')

@login_required
def generateView(request):
    amount = 150
    receiver = Points.objects.get(owner=request.user)
    receiver.points = receiver.points + amount
    receiver.save()
    return redirect('/')

@login_required
def inspectView(request):
    query = Points.objects.raw('SELECT points FROM point_site_points WHERE owner = %s', (request.owner))
    return render(request, 'point_site/inspect.html',{'query': query})