from django.shortcuts import render
from courses.models import *

def students_view(request):

    # Return Sensor additional details from DeviceInfo Model
    student_list = Student.objects.all()

    # Set context and page variables for returning data
    context = {"student_list": student_list}
    page_url = "students.html"

    # Return sensor info to html page
    return render(request, page_url, context)


def lecturers_view(request):

    # Return Sensor additional details from DeviceInfo Model
    lecturer_list = Lecturer.objects.all()

    # Set context and page variables for returning data
    context = {"lecturer_list": lecturer_list}
    page_url = "lecturers.html"

    # Return sensor info to html page
    return render(request, page_url, context)


def courses_view(request):

    # Return Sensor additional details from DeviceInfo Model
    course_list = Course.objects.all()

    # Set context and page variables for returning data
    context = {"course_list": course_list}
    page_url = "courses.html"

    # Return sensor info to html page
    return render(request, page_url, context)