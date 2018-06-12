from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from axes.decorators import axes_dispatch


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

axes_dispatch
@method_decorator(csrf_exempt, name='dispatch')
def index(request):
    return render(request, 'website/index.html')

def lockout(request):
    return render(request, 'website/lockout.html')

@login_required
def home(request):
    return render(request, 'website/home.html')


@login_required
def commands(request):
    commands = {
        'ls': 
        {
            'desc': 'List files in directory',
            'parameters': {
                'l': {
                    'desc': 'Print the files as List',
                },
                'a': {
                    'desc': 'Show all files (includes hidden files)',
                }
            }
        },
        'pwd': 
        {
            'desc': 'Print current working path',
        },
        'pwd': 
        {
            'desc': 'Print current working path',
        },
        'date': 
        {
            'desc': 'Print the current date considering the configured locales',
            'parameters': {
                'l': {
                    'desc': 'Print the files as List',
                },
                'a': {
                    'desc': 'Show all files (includes hidden files)',
                }
            }
        }
    }
    return render(request, 'website/commands.html')
