from django.shortcuts import render
import os
import numpy as np
import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def page1(request):
    return render(request, 'page1.html', {})
