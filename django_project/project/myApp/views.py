# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world.")


def detail(request, num):
    return HttpResponse("detail--%s" % num)
