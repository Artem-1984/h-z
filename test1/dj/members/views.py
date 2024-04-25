from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from django.contrib.auth import authenticate,login


def first(request):
    template = loader.get_template('first.html')

    return HttpResponse(template.render())
def City_leagers(request):
    template = loader.get_template('City_leaders.html')
    return HttpResponse(template.render())
def City_news(request):
    template = loader.get_template('City_news.html')
    return HttpResponse(template.render())

def Contact(request):
    template = loader.get_template('Contact_numbers_of_town_services.html')
    return HttpResponse(template.render())
def Facts(request):
    template = loader.get_template('Facts_about_the_city.html')
    return HttpResponse(template.render())
def History(request):
    template = loader.get_template('History.html')
    return HttpResponse(template.render())
def History_fotos(request):
    template = loader.get_template('foto.html')
    return HttpResponse(template.render())
def History_people(request):
    template = loader.get_template('People.html')
    return HttpResponse(template.render())

def Error(request,exception):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())


# def back_History(request):
#     context = {'title': 'History'}
#     return render(request, 'History.html', context)