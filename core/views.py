from django.http import request
from core.models import Evento
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#def index(request):
    #return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/') 



def submit_login(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        usuario=authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuário ou senha inválidos")    

    return redirect('/')    



@login_required(login_url='/login/')
def lista_eventos(request):
    usuario=request.user
    #o comando abaixo ("objectos.filter") seleciona só objetos por usuário ou pelo filtro determinado
    evento=Evento.objects.filter(usuario=usuario)
    #comando abaixo ("Objects.all") seleciona todos os objetos da agenda.
    #evento=Evento.objects.all
    dados={'eventos':evento}
    return render(request, 'agenda.html', dados)