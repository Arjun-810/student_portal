from django.urls import path
from .import views

urlpatterns = [
    path('marks/', views.students_marks)
]