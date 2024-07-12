from django.shortcuts import render
from .models import New


# Create your views here.
def index(request):
    news = New.objects.all()
    return render(request, 'index.html', context={'news': news})

def detail(request, slug):
    new = New.objects.get(slug__iexact=slug)
    return render(request, 'details.html', context={'new':new})