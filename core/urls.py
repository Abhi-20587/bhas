
from django.urls import path
from .views import Abc
urlpatterns = [
    
    path('',Abc.as_view(),name="abc")
]