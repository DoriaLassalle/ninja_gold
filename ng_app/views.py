from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
import random

# Create your views here.

def home(request):
    if "gold" not in request.session:
        request.session["gold"]=0

    return render(request, "index.html")


def processMoney(request):
    if "activityList" not in request.session:
        request.session["activityList"]=[]

    print(request.POST)
    opcion=request.POST["btn"]
    print (opcion)
    if opcion=="1":
        money=farmRandom()
        request.session["gold"]+=money
        request.session["activity"]=f"La Granja te ha otorgado {money} lingotes de Oro!...{strftime('%H:%M  %w/%m/%Y.',localtime())}"
        request.session["activityList"].append(request.session["activity"])
    elif opcion=="2":
        money=caveRandom()
        request.session["gold"]+=money
        request.session["activity"]=f"La Cueva te ha otorgado {money} lingotes de Oro!...{strftime('%H:%M  %w/%m/%Y.',localtime())}"
        request.session["activityList"].append(request.session["activity"])
    elif opcion=="3":
        money=houseRandom()
        request.session["gold"]+=money
        request.session["activity"]=f"La Casa te ha otorgado {money} lingotes de Oro!...{strftime('%H:%M  %w/%m/%Y.',localtime())}"
        request.session["activityList"].append(request.session["activity"])
    elif opcion=="4":
        money=casinoRandom()
        luck=random.randint(1,2)
        print(luck)
        if luck==1:
            request.session["gold"]+=money
            request.session["activity"]=f"Le has ganado al Casino {money} lingotes de Oro!!!...{strftime('%H:%M  %w/%m/%Y.',localtime())}"
            request.session["activityList"].append(request.session["activity"])
        elif luck==2:
            request.session["gold"]-=money
            request.session["activity"]=f"Lo siento :( el Casino te ganó {money} lingotes de Oro!...{strftime('%H:%M  %w/%m/%Y.',localtime())}"
            request.session["activityList"].append(request.session["activity"])
    print(request.session["activityList"])
    return redirect("/")

def restart(request):
    request.session["activityList"]=[]
    request.session["gold"]=0
    return redirect("/")


def farmRandom():
    farm=random.randint(10, 20)
    print(farm)
    return farm

def caveRandom():
    cave=random.randint(5, 10)
    print(cave)
    return cave

def houseRandom():
    house=random.randint(2,5)
    print(house)
    return house

def casinoRandom():
    casino=random.randint(0, 50)
    print(casino)
    return casino