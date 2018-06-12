from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'website/index.html')

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
