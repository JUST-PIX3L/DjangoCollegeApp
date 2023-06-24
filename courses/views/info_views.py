from django.shortcuts import render
from courses.models import *

def students_info_view(request):

    # Return Sensor additional details from DeviceInfo Model
    student_info = Student.objects.first()

    # Set context and page variables for returning data
    context = {"student_info": student_info}
    page_url = "students_info.html"

    # Return sensor info to html page
    return render(request, page_url, context)


def lecturers_info_view(request):

    # Return Sensor additional details from DeviceInfo Model
    lecturer_info = Lecturer.objects.first()

    # Set context and page variables for returning data
    context = {"lecturer_info": lecturer_info}
    page_url = "lecturers_info.html"

    # Return sensor info to html page
    return render(request, page_url, context)