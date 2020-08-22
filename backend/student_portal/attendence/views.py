from django.shortcuts import render
from django.http import JsonResponse
from .models import attendence
import json
from students.models import studentsDetails


def students_attendence(request):
    if request.method=="POST":
        student_data = json.loads(request.body)
        student_id = student_data['student_id']
        return_data=attendence.objects.filter(studentsDetails_id__id__contains=student_id).values('pre_prcentage','pre_no','abs_no')
        return JsonResponse(list(return_data),safe=False)
