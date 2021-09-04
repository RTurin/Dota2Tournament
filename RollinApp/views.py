from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from .models import *
from django.views.generic import TemplateView,DetailView
from django.views import generic

from .models import *
import json
import requests
import pprint
class HomeView(TemplateView):
    template_name = "StorePages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # cart = Cart.objects.get(id=2)

        # print("Customer Name:",cart.customer)
        # print(cart.total)
        # context['cart'] = cart



        # context ['cart'] =cart
        return context

class TestView(TemplateView):
    template_name= "StorePages/test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # teamData = Team.objects.get(name="OG")

        # teamData1 = Team.objects.all()
        # print(teamData)


        # context['teamData'] = teamData

        # context['teamData1'] = teamData1

        tournament = Tournament.objects.get(title= "OGA Dota PIT Invitational")
        # print(tournament)
        context['tournament']= tournament

        getMatches = Match.objects.get(id= 1)
        print(getMatches.matchType)
        print(getMatches.tournament.title)

        context['getMatches'] = getMatches
        

        return context






def home1(request):
    response = requests.get('https://api.opendota.com/api/matches/6156080212').json()
    # geodata = response.json()
    
    context = {
        'response':response
    }
    return render(request, "StorePages/test1.html", context)



    
