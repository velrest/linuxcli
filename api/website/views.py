from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from axes.decorators import axes_dispatch
from subprocess import run, PIPE
from django.conf import settings


def register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username=username, password=password)
    user.save()
    authuser = authenticate(username=username, password=password)
    login(request, authuser)
    return redirect('/home/')

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/home/')
    else:
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

def index(request):
    if request.user.is_authenticated:
        return redirect('/home')
    return render(request, 'website/index.html')

def lockout(request):
    return render(request, 'website/lockout.html')

@login_required
def commands(request, command=None):
    commands = settings.COMMANDS
    if request.method == 'GET':
        return render(request, 'website/commands.html', {'commands':commands})
    elif request.method == 'POST':        
        if commands.get(command):
            parameters = commands.get(command).get('parameters')
            if not parameters:
                parameters = {}
            exec_list = [command]
            exec_list.extend(['-{}'.format(k) for k,v in request.POST.items() if parameters.get(k)])
            print(exec_list)
            return render(request, 'website/output.html', { 'output': run(exec_list, stdout=PIPE).stdout.decode('utf-8'), 'command': ' '.join(exec_list) })
        else:
            return redirect('/home')
