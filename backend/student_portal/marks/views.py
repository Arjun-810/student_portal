from django.shortcuts import render
from django.http import JsonResponse
from .models import marks
import json
from students.models import studentsDetails


def students_marks(request):
    if request.method=="POST":
        student_data = json.loads(request.body)
        student_id = student_data['student_id']
        return_data=marks.objects.filter(studentsDetails_id__id__contains=student_id).values('id','test_name','Mathematcs','Human_values','DS','COA','DSL')
        return JsonResponse(list(return_data),safe=False)
