from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def TestFn(request):
    #print('hloooo')
    return HttpResponse('hlooooo')
def TestFn2(request):
    return HttpResponse('HIIIIII')
def TestFn3(request):
    return render(request,'index.html')