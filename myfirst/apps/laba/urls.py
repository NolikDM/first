from django.urls import path, include, re_path

from .import views

urlpatterns = [
    re_path(r'downf$', views.download),
    re_path(r'downf/$', views.download),
    re_path(r'crdir$', views.create),
    re_path(r'crdir/$', views.create),
    re_path(r'deldir$', views.delete),
    re_path(r'deldir/$', views.delete),
    re_path(r'^', views.index),
]
