from django.urls import path
from courses import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('templates/homepage.html', views.homepage_view, name='homepage.html'),

    path('templates/students.html', views.students_view, name='students.html'),
    path('templates/lecturers.html', views.lecturers_view, name='lecturers.html'),
    path('templates/courses.html', views.courses_view, name='courses.html'),
]