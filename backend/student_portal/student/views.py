from django.shortcuts import render
from .models import studentDetails
from django.http import JsonResponse
import json
# Create your views here.
def studentLogin(request):
    if request.method == "POST":
        login_data = json.loads(request.body)
        mailId = login_data['mailId']
        password = login_data['password']
        if studentDetails.objects.filter(mailId__contains=mailId,password__contains=password).filter(mailId=mailId,password=password).exists():
           return JsonResponse("OK",safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)