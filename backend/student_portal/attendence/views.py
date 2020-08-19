from django.shortcuts import render
from django.http import JsonResponse
from .models import attendence
import json
from students.models import studentsDetails


def students_attendence(request):
    if request.method=="POST":
        student_data = json.loads(request.body)
        student_id = student_data['student_id']
        return_data=attendence.objects.filter(studentsDetails_id__id__contains=student_id).values('id','p1','p2','p3','p4','p5','p6','p7','p8')
        return JsonResponse(list(return_data),safe=False)
