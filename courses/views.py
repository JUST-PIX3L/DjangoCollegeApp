from django.shortcuts import render

def homepage_view(request):
    return render(request, 'homepage.html', {})

def lecturers_view(request):
    return render(request, 'lecturers.html', {})

def students_view(request):
    return render(request, 'students.html', {})

def courses_view(request):
    return render(request, 'courses.html', {})