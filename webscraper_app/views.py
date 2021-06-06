from django.shortcuts import render
from bs4 import beautifulsoup

def home(request):
    return render(request, "base.html", )

def new_search(request):
    search_data = request.POST.get('search')
    print(search_data)
    context = {
        'search_term' : search_data,
    }
    return render(request, "content/new_search.html", context,)
