from django.shortcuts import render
from django.http import HttpRequest, HttpResponse ,Http404
from django.core.exceptions import ObjectDoesNotExist

from .models import Busines


def create_new_busines(request:HttpRequest):
    new_business = Busines(
        NIP=request.POST['NIP'],
        name=request.POST['name'],
        owner=request.POST['owner']
    )
    new_business.save()

def edit_busines(request:HttpRequest,busines:Busines):
    busines.NIP = request.POST['NIP']
    busines.name = request.POST['name']
    busines.owner = request.POST['owner']
    busines.save()

##################### CRUD ########################
def create(request:HttpRequest):
    if request.method == 'GET':
        return render(request,'busines/create.html')
    if request.method=="POST":
        create_new_busines(request)
        return HttpResponse("Created New Busines Success")

def retrive(request:HttpRequest):
    all_business = Busines.objects.all()
    context = { 'dataset': all_business }
    return render(request,'busines/retrive.html',context)

def update(request:HttpRequest,id):
    try:
        busines = Busines.objects.get(pk=id)
        if request.method == 'GET':
            return render(request,'busines/update.html',{'busines':busines})
        if request.method == 'POST':
            edit_busines(request,busines)
            return HttpResponse("Updating Busines Success")
    except ObjectDoesNotExist:
        return Http404("Busines does not exist")
          
def delete(request:HttpRequest,id):
    try:
        busines = Busines.objects.get(pk=id)
        busines.delete()
        return HttpResponse("Deleting Busines Success")
    except ObjectDoesNotExist:
        return Http404("Busines does not exist")
    
'''
How to heandel ERRORS
'''
