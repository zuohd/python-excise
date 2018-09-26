# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Grades, Children


def index(request):
    return HttpResponse("Hello world.")


def detail(request, num):
    return HttpResponse("detail--%s" % num)


def grades(request):
    gradesList = Grades.objects.all()
    return render(request, "myApp/grades.html", {'grades': gradesList})


def children(request):
    childrenList = Children.childObj.get_queryset()
    return render(request, "myApp/children.html", {'children': childrenList})


def gradesChildren(request, gid):
    childrenList = Grades.objects.get(pk=gid).children_set.all()
    return render(request, "myApp/children.html", {'children': childrenList})


def addChild(request):
    grade = Grades.objects.get(pk=1)
    child = Children.childObj.createChild("Jessica", False, 30, "I'm beauty", grade)
    child.save()
    return HttpResponse("The object inserted")


def ChildrenPage(request, page):
    page = int(page);
    childrenList = Children.childObj.all()[(page - 1) * 3:page * 3]
    return render(request, "myApp/children.html", {'children': childrenList})
