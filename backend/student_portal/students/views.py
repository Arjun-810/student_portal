from django.shortcuts import render
from .models import studentsDetails
from django.http import JsonResponse
import json
# Create your views here.
def studentsLogin(request):
    if request.method == "POST":
        login_data = json.loads(request.body)
        mailId = login_data['mail_id']
        password = login_data['password']
        if studentsDetails.objects.filter(mail_id__contains=mailId,password__contains=password).filter(mail_id=mailId,password=password).exists():
           return JsonResponse("OK",safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)

def studentsBirthday(request):
    if request.method=="GET": 
        return_data=studentsDetails.objects.filter(status__contains="OK").values('id',  'dob', 'Name', 'Roll_no', 'course', 'semister')
        return JsonResponse(list(return_data),safe=False)
