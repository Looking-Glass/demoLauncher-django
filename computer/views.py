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
from django.views.decorators.csrf import csrf_exempt 
from models import Computer

@csrf_exempt
def update(request):
    name=request.POST.get("name")
    existingApps=request.POST.get("existingApps","")
    runningApp=request.POST.get("runningApp","")
    computer, created=Computer.objects.get_or_create(name=name)
    computer.existingApps=existingApps
    computer.runningApp=runningApp
    action=computer.action
    computer.action=""
    computer.save()
    return HttpResponse(action)

@csrf_exempt
def action(request):
    val=True
    name=request.POST.get("computer","")
    action=request.POST.get("action","")
    app=request.POST.get("app","")
    try:
        computer=Computer.objects.get(name=name)
        computer.action="%s, %s" % (action,app)
        computer.save()
    except SomeModel.DoesNotExist:
        computer=None
        return HttpResponse('ok')


