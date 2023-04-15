from django.shortcuts import render 
import datetime

# Create your views here.
def newyear(request):
    newyear = datetime.datetime.now()
    return render(request, "newyear/newyear.html", {
        "newyear": newyear.day == 1 and newyear.month == 1
    })