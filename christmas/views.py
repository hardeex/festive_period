from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "xmas/index.html", {
        "now": now
    })

def christmas(request):
    xmas = datetime.datetime.now()
    return render(request, "xmas/xmas.html", {
        "xmas":xmas.day == 25 and xmas.month == 12
    })
