from django.shortcuts import render
from BackendApi.models import Users
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


# Create your views here.

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        username = payload['username']
        dbemail = payload['email']
        dbpassword = payload['password']
        user = Users(login = username, password = dbpassword, email = dbemail)
        try:
            user.save(force_insert = True)
            response = json.dumps([{'Sukces': 'Pomyslnie dodano uzytkownika'}])
        except Exception as e:
            response = json.dumps([{'Blad': str(e)}])
    return HttpResponse(response, content_type='text/json')
    
        

    

