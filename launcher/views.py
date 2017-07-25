from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.html import escape
from django.conf import settings
from django.http import Http404  
import logging
import datetime
import subprocess
import os
import json
import requests
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt 
from computer.models import Computer
import sys
#import HttpRequest
from django.urls import reverse

def home(request):
    time_threshhold = datetime.now() - timedelta(minutes=1) #get all computers w/pings in the last minute as 'active' computers
    activeComputers=Computer.objects.filter(lastUpdated__gt=time_threshhold)
    inactiveComputers=Computer.objects.filter(lastUpdated__lt=time_threshhold)
    return render(request, "launcher/home.html", {"activeComputers": activeComputers, "inactiveComputers" : inactiveComputers})

def computer(request, computerName="null"):
    actionURL=request.build_absolute_uri(reverse('action'))
    try:
        computer=Computer.objects.get(name=computerName)
    except Computer.DoesNotExist:
        computer=null
    return render(request, "launcher/computer.html", {"computer":computer, "actionURL":actionURL})

@csrf_exempt
def action(request):
    val=True
    name=request.POST.get("computer")
    action=request.POST.get("action")    
    app=request.POST.get("app")    
    computer=Computer.objects.get(name=name)
    computer.action="%s,%s" % (action,app)
    computer.runningApp=app
    computer.save()
    return HttpResponse(computer.action)



