from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def create(request:HttpRequest):
    return HttpResponse("Hello, Form Create")

def retrive(request:HttpRequest):
    return HttpResponse("Hello, Form Retrive")

def update(request:HttpRequest,id):
    return HttpResponse(f"Hello, Form Update id={id}")
    
def delete(request:HttpRequest,id):
    return HttpResponse(f"Hello, Form Delete id={id}")
    
