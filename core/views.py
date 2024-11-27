from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
 

def sample1(request):
    return JsonResponse({"message":"Hello JSON"}) 

def sample2(request):
    return JsonResponse({"text":"Hello Charan"})
