from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
from students.models import Student
def index(request):
    return render(request,'index.html')

def adminpannel(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    q=Student(username=username,password=password)
    q.save()
    return render(request,'admin.html')