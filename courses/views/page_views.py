from django.shortcuts import render
from courses.models import *

def homepage_view(request):
    return render(request, 'homepage.html', {})