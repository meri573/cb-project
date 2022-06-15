from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from.models import Points
from django.contrib.auth.models import User
from django.db import connection

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

@csrf_exempt
@login_required
def sendView(request):

    receiver = User.objects.get(username=request.GET.get('to'))
    receiver = Points.objects.get(owner=receiver)
    sender = Points.objects.get(owner=request.user)
    amount = int(request.GET.get('amount'))

    sender.points = sender.points - amount
    receiver.points = receiver.points + amount
    sender.save()
    receiver.save()
    return redirect('/')

@login_required
def generateView(request):
    # if not request.user.is_staff:
        # return redirect('/')

    amount = 150
    receiver = Points.objects.get(owner=request.user)
    receiver.points = receiver.points + amount
    receiver.save()
    return redirect('/')

@login_required
def inspectView(request):
    # "1\' UNION SELECT password FROM auth_user WHERE username like 'admin"
    query = "SELECT points FROM point_site_points WHERE id = '%s'" % request.POST.get('id')
    print(query)
    results = sql(query)

    # results = Points.objects.get(id = int(request.POST.get('id')))

    return render(request, 'point_site/inspect.html',{'results': results})

def sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result
