# Create your views here.
from django.db.models import Max, Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Grades, Children


def index(request):
    return HttpResponse("Hello world.")


def detail(request, num):
    return HttpResponse("detail--%s" % num)


def grades(request):
    gradesList = Grades.objects.all()
    # gradesList = Grades.objects.filter(ggirlnum__gte=F('gboynum'))

    return render(request, "myApp/grades.html", {'grades': gradesList})


def children(request):
    # childrenList = Children.childObj.get_queryset()
    childrenList = Children.childObj.filter(Q(pk__lte=2) | Q(sage__gt=30))
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


def childrenSearch(request):
    # childrenList = Children.childObj.filter(pname__contains="om")
    # childrenList = Children.childObj.filter(pname__startswith="so")
    childrenList = Children.childObj.filter(pk__in=[2, 4, 5])
    maxAge = Children.childObj.aggregate(Max('sage'))
    print(maxAge)
    childrenList = Children.childObj.filter(sgrade__gname__contains="python")
    return render(request, "myApp/children.html", {'children': childrenList})


def attributes(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("Attribute.")


def getparameter(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + b + c)
