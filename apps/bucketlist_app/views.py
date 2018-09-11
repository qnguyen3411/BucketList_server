from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
# Create your views here.
def index(self):
    return redirect("/tasks")

@csrf_exempt
def tasks(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        print(tasks)
        return JsonResponse({'tasks': list(tasks.values())})
    else :
        print("WE GOT A POST REQUEST OVA HEre")
        print(request.POST)
        if 'objective' in request.POST:
            Task.objects.create(objective=request.POST['objective'])
        return HttpResponse("YEEEEEEEEEEEEEEEEEEBOI")