from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^grades/$', views.grades),
    url(r'^children/$', views.children),
    url(r'^children/(\d+)/$', views.ChildrenPage),
    url(r'^grades/(\d+)$', views.gradesChildren),
    url(r'^addchild/$', views.addChild),
    url(r'^childrensearch/$', views.childrenSearch),
    url(r'(\d+)/$', views.detail),

]
