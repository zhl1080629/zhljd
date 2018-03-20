from django.conf.urls import url
from geekpy import views

urlpatterns = [
    url(r'^index/$', views.index)
]