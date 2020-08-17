from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.studentsLogin),
    path('birthday/', views.studentsBirthday)
]