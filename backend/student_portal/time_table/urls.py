from django.urls import path
from .import views

urlpatterns = [
    path('table/', views.students_time_table)
]