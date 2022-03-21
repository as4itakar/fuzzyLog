from django.shortcuts import render
from .fuzzy import Fuzzy
from django.http import HttpResponse
from matplotlib import pylab as plt
from matplotlib import colors
import numpy as np
import math


def index(request):
    return render(request, 'main/index.html')


def res(request):
    if request.method == "POST":
        price = request.POST.get("price")
        speed = request.POST.get("speed")
        family = request.POST.get("family")
        beauty = request.POST.get("beauty")
        comfort = request.POST.get("comfort")
        salon = request.POST.get("salon")
        fuz = Fuzzy(speed, price, family, beauty, comfort, salon)
        result = fuz.calc()
        return render(request,'main/result.html', {'result': result})










