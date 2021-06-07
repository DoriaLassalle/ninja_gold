from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
import random


def start(request):
    request.session["activityList"]=[]
    request.session["gold"]=0
    request.session["meta"]=0
    return render(request, "inicio.html")

def home(request):
    if "gold" not in request.session:
        request.session["gold"]=0         

    if request.method=="POST":
        metaDelUsuario=request.POST["goldMax"]
        request.session["meta"]=metaDelUsuario
        jugadas=request.POST["moves"]
        request.session["jugadas"]=jugadas
        request.session["player"]=request.POST["player"]
      
    if request.session["gold"]==request.session["meta"] or int(request.session["gold"]) > int(request.session["meta"]) and len(request.session["activityList"]) <= int(request.session["jugadas"]) :
        ganancia=request.session["gold"]              
        return render(request, "win.html")

    if len(request.session["activityList"]) > int(request.session["jugadas"]) and int(request.session["gold"]) < int(request.session["meta"]):
      
        return render(request, "lose.html")

    return render(request, "index.html")


def processMoney(request):
    if "activityList" not in request.session:
        request.session["activityList"]=[]       
        
    opcion=request.POST["btn"]
   
    if opcion=="1":
        money=farmRandom()
        request.session["gold"]+=money
        request.session["activity"]=f"Working at the Farm gave you {money} golds! ...{strftime('%H:%M  %w/%m/%Y.',localtime())}"
        request.session["activityList"].insert(0,request.session["activity"])

    elif opcion=="2":
        money=caveRandom()
        request.session["gold"]+=money
        request.session["activity"]=f"Spend one night at the Cave gave you {money} golds! ...{strftime('%H:%M  %w/%m/%Y.',localtime())}"
        request.session["activityList"].insert(0,request.session["activity"])

    elif opcion=="3":
        money=houseRandom()
        request.session["gold"]+=money
        request.session["activity"]=f"Earned {money} golds for cleaning the House! ...{strftime('%H:%M  %w/%m/%Y.',localtime())}"
        request.session["activityList"].insert(0,request.session["activity"])

    elif opcion=="4":
        money=casinoRandom()
        luck=random.randint(1,2)
        
        if luck==1:
            request.session["gold"]+=money
            request.session["activity"]=f"Great!!  You won {money} golds from the Casino!!! ...{strftime('%H:%M  %w/%m/%Y.',localtime())}"
            request.session["activityList"].insert(0,request.session["activity"])
        elif luck==2:
            request.session["gold"]-=money
            request.session["activity"]=f"The Casino beats you :( ...you lost {money} golds! ...{strftime('%H:%M  %w/%m/%Y.',localtime())}"            
            request.session["activityList"].insert(0,request.session["activity"])
    
    return redirect("/continue")

def restart(request):
    request.session["activityList"]=[]
    request.session["gold"]=0
    request.session["meta"]=0
    return redirect("/")


def farmRandom():
    farm=random.randint(10, 20)
    return farm

def caveRandom():
    cave=random.randint(5, 10)
    return cave

def houseRandom():
    house=random.randint(2,5)
    return house

def casinoRandom():
    casino=random.randint(0, 50)   
    return casino