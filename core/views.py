from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
class Abc(View):
    def get(self,requests):
        return HttpResponse("Hey This is Heroku App")