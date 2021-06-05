from django.shortcuts import render

def home(request):
    return render(request, "base.html", )

def new_search(request):
    return render(request, "new_search.html", )
