# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Grades


def index(request):
    return HttpResponse("Hello world.")


def detail(request, num):
    return HttpResponse("detail--%s" % num)


def grades(request):
    gradesList = Grades.objects.all()
    return render(request, "myApp/grades.html", {'grades': gradesList})


def children(request):
    pass
