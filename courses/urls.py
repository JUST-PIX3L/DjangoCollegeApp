from django.urls import path
from courses import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
]