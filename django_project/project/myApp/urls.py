from django.conf.urls import re_path

from . import views

app_name = "myApp"
urlpatterns = [
    re_path(r'^$', views.index),

    re_path(r'^grades/$', views.grades),
    re_path(r'^children/$', views.children),
    re_path(r'^children/(\d+)/$', views.ChildrenPage),
    re_path(r'^grades/(\d+)$', views.gradesChildren),
    re_path(r'^addchild/$', views.addChild),
    re_path(r'^childrensearch/$', views.childrenSearch),
    re_path(r'(\d+)/$', views.detail),

]
