from django.shortcuts import render
from django.http import HttpResponse


class Dolphin: 
    def __init__(self, name, region, description, status):
        self.name = name
        self.region = region
        self.description = description
        self.status = status

dolphins = [
    Dolphin('Amazon River Dolphin','South America','freshwater dolphins','ENDANGERED'),
    Dolphin('Atlantic Humpback Dolphin','Atlantic','humpback','CRITICAL'),
    Dolphin('Chilean Dolphin','South America','White-bellied','NEAR THREATHENED')
]





# Create your views here.
def home(request):
    return HttpResponse('<h1> Hello </h1>')

def about(request):
    return render(request, 'about.html')

def dolphins_index(request):
    return render(request, 'dolphins/index.html', {'dolphins': dolphins})
