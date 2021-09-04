from django.conf.urls import url
from django.urls import path


from .views import *
app_name = "RollinApp"
urlpatterns = [
    path('test/',HomeView.as_view(),name="home"),
    path('',TestView.as_view(),name="test"),

    path('test2/',home1,name="test2"),


]