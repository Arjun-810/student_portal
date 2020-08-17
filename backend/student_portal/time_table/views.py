from django.shortcuts import render
from django.http import JsonResponse
from .models import timtTable
import json
from students.models import studentsDetails


def students_time_table(request):
    if request.method=="POST":
        student_data = json.loads(request.body)
        semister = student_data['semister']
        course = student_data['course']
        branch = student_data['branch']
        day = student_data['day']
        return_data=timtTable.objects.filter(day__contains=day,semister__contains=semister,course__contains=course,branch__contains=branch).values('id','p1','p2','p3','p4','p5','p6','p7','p8','time1','time2','time3','time4','time5','time6','time7','time8',)
        return JsonResponse(list(return_data),safe=False)
