from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'(\d+)/$', views.detail),
    url(r'^grades/', views.grades),
    url(r'^children/', views.children)
]
