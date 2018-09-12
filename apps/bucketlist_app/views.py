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
        return JsonResponse({'tasks': list(tasks.values())})
    else :
        if 'objective' in request.POST:
            Task.objects.create(objective=request.POST['objective'])
        return HttpResponse("YEEEEEEEEEEEEEEEEEEBOI")

@csrf_exempt
def update_tasks(request, id):
    if request.method == "POST":
        try:
            this_task = Task.objects.get(id=id)
            this_task.objective = request.POST['objective']
            this_task.save()
        except:
            print("ERROR TRYING TO UPDATE")
    return HttpResponse("YEEEEEEEEEEEEEEEEEEBOI")

def delete_tasks(request, id):
    try:
        this_task = Task.objects.get(id=id)
        this_task.delete()
        print("DELETE SUCCESSFUL")
    except:
        print("ERROR TRYING TO DELETE")
    return HttpResponse("YEEEEEEEEEEEEEEEEEEBOI")
