from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader  
from .models import Players

# Create your views here.
def players(request):
    myPlayers = Players.objects.all().values()
    template = loader.get_template('players_info.htm')
    context = {
        'myPlayers' : myPlayers,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    myPlayer = Players.objects.get(id=id)
    template = loader.get_template('player_details.htm')
    context = {
        'myPlayer' : myPlayer, 
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.htm')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('testEnv.htm')
    context = {
        'justTesting': 'Testing is successful',
    }
    return HttpResponse(template.render(context,request))