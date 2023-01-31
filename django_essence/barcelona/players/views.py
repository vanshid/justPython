from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader  
from .models import Players
from django.db.models import Q

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

# ''' GET DATA
# values_list('firstName') -> Specific column 
# .filter('','') -> kwargs returns rows 
# objects.filter(firstName='').values() | Member.objects..  -> OR
# objects.filter(Q(firstName='') | Q(firstName='')) -> Q library  
# '''

# ''' WHERE IN DJANGO
# Fields Look-up
# .filter(firstname__startswith='L');
# https://www.w3schools.com/django/django_queryset_filter.php
# '''

# ''' SORT 
# order_by('firstname','') -> ASEC
# order_by('-firstname') -> DESC 
# '''

def testing(request):
    testingPlayers = Players.objects.all()
    template = loader.get_template('testEnv.htm')
    context = {
        'testingPlayers' : testingPlayers ,
    }
    return HttpResponse(template.render(context,request))