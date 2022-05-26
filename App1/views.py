from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from typing import List
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from App1.forms import CreatorsForm, GamesForm, RegisterForm, UserForm
from App1.models import Creators, Games, User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):

      return render(request, "App1/inicio.html")

def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST) 

        if form.is_valid():
            
            username=form.cleaned_data.get('username') 
            password=form.cleaned_data.get('password')    

            user=authenticate(username=username, password=password)

            if user:

                login(request, user)

               
                return render(request, "App1/inicio.html", {'message':f"Welcome {user}"}) 

        else: 
    
            return render(request, "App1/inicio.html", {'message':"Incorrect information, user not found"})

    else:
            
        form = AuthenticationForm()

    return render(request, "App1/login.html", {'form':form})      

def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            username=form.cleaned_data['username']

            form.save()
            
            return render(request, "App1/inicio.html", {'mensaje':"User successfully created"})
    
    else:

        form = RegisterForm()
    
    
    return render(request, "App1/register.html", {'form':form})

def users(request):

      if request.method == 'POST':

            Formulario1 = UserForm(request.POST)

            print(Formulario1)

            if Formulario1.is_valid: 

                  data = Formulario1.cleaned_data

                  user = User(name=data['name'], city=data['city'], age=data['age'], email=data['email']) 

                  user.save()

                  return render(request, "App1/inicio.html")

      else: 

            Formulario1 = UserForm()

      return render(request, "App1/users.html", {"Formulario1":Formulario1})

def games(request):

      if request.method == 'POST':

            Formulario2 = GamesForm(request.POST)

            print(Formulario2)

            if Formulario2.is_valid: 

                  data = Formulario2.cleaned_data

                  games = Games(name=data['name'], developer=data['developer'], popularity=data['popularity'], type=data['type']) 

                  games.save()

                  return render(request, "App1/inicio.html")

      else: 

            Formulario2 = GamesForm()

      return render(request, "App1/games.html", {"Formulario2":Formulario2})

def creators(request):

      if request.method == 'POST':

            Formulario3 = CreatorsForm(request.POST)

            print(Formulario3)

            if Formulario3.is_valid: 

                  data = Formulario3.cleaned_data

                  creators = Creators(username=data['username'], platforms=data['platforms'], subscriptions=data['subscriptions']) 

                  creators.save()

                  return render(request, "App1/inicio.html")

      else: 

            Formulario3 = CreatorsForm()

      return render(request, "App1/creators.html", {"Formulario3":Formulario3})

def browsingGames(request):
    return render(request, "App1/browsingGames.html")      

def search(request):

    if request.GET["name"]:

        name = request.GET['name']

        games = Games.objects.filter(name__icontains=name)
    
        return render(request, "App1/search.html", {"games":games, "name":name})

    else:

        answer = "No data sent"
        
    return render(request, "App1/inicio.html", {"answer":answer})

class GamesList(ListView):

      model = Games 
      template_name = "App1/gamesList.html"


class GamesDetail(DetailView):

      model = Games
      template_name = "App1/gamesDetail.html"


class GamesCreation(CreateView):

      model = Games
      success_url = "/App1/games/list" 
      fields = ['name', 'developer', 'popularity', 'type']


class GamesUpdate(UpdateView):

      model = Games
      success_url = "/App1/games/list"
      fields  = ['name', 'developer', 'popularity', 'type']


class GamesDelete(DeleteView):

      model = Games
      success_url = "/App1/games/list"

class CreatorsList(ListView):

      model = Creators 
      template_name = "App1/creatorsList.html"


class CreatorsDetail(DetailView):

      model = Creators
      template_name = "App1/creatorsDetail.html"


class CreatorsCreation(CreateView):

      model = Creators
      success_url = "/App1/creators/list" 
      fields = ['username', 'platforms', 'subscriptions']


class CreatorsUpdate(UpdateView):

      model = Creators
      success_url = "/App1/creators/list"
      fields  = ['username', 'platforms', 'subscriptions']


class CreatorsDelete(DeleteView):

      model = Creators
      success_url = "/App1/creators/list"

class UsersList(ListView):

      model = User 
      template_name = "App1/usersList.html"


class UsersDetail(DetailView):

      model = User
      template_name = "App1/usersDetail.html"


class UsersCreation(CreateView):

      model = User
      success_url = "/App1/users/list" 
      fields = ['name', 'city', 'age', 'email']


class UsersUpdate(UpdateView):

      model = User
      success_url = "/App1/users/list"
      fields  = ['name', 'city', 'age', 'email']


class UsersDelete(DeleteView):

      model = User
      success_url = "/App1/users/list"                                  