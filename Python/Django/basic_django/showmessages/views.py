from django.shortcuts import render


def index(request):
    items = [
        {'name': 'ken', 'age': "dad", 'tell': "052522", "addess": 5252252},
        {'name': 'ken', 'age': "dad", 'tell': "052522", "addess": 5252252},
        {'name': 'ken', 'age': "dad", 'tell': "052522", "addess": 5252252},
        {'name': 'ken', 'age': "dad", 'tell': "052522", "addess": 5252252},
        {'name': 'ken', 'age': "dad", 'tell': "052522", "addess": 5252252},
        {'name': 'ken', 'age': "dad", 'tell': "052522", "addess": 5252252},
    ]
    return render(request, 'index.html', {'items': items, })
