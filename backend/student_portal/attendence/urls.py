from django.urls import path
from .import views

urlpatterns = [
    path('daily/', views.students_attendence)
]