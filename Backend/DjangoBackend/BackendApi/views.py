from django.shortcuts import render
from BackendApi.models import Users
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework_jwt.settings import api_settings
import json
import jwt
from django.conf import settings



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
            response = json.dumps({'Sukces': 'Pomyslnie dodano uzytkownika'})
        except Exception as e:
            response = json.dumps({'message': str(e)})
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def get_user(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        get_email = payload['email']
        get_password = payload['password']
        try:
            user = Users.objects.get(email=get_email, password=get_password)


            access_token_payload = {
            'email': user.email,
            'login': user.login,
            'password': user.password
            }

            token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')

            response = json.dumps({'userId': user.email, 'accessToken': format(token)})
            return HttpResponse(response, content_type='text/json')
        except Exception as e:
            response = json.dumps({'message': str(e)})
            return HttpResponse(response, content_type='text/json', status = 403)

@csrf_exempt
def add_subject(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['subject_name']
        token = payload['token']
        try:
            user_data = jwt.decode(token, None, None)
            print(user_data['email'])

            response=json.dumps({'message': user_data['email']})
            return HttpResponse(response, content_type='text/json')
        except Exception as e:
            response = json.dumps({'message': str(e)})
            return HttpResponse(response, content_type='text/json', status = 403)

@csrf_exempt
def add_teacher(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        surname = payload['surname']
        email = payload['email']
        token = payload['token']
        sub_list = payload['list_of_subjects']
        try:
            user_data = jwt.decode(token, None, None)
            print(user_data['email'])
            response=json.dumps({'message': sub_list})
            return HttpResponse(response, content_type='text/json')
        except Exception as e:
            response = json.dumps({'message': str(e)})
            return HttpResponse(response, content_type='text/json', status = 403)

@csrf_exempt
def add_classroom(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        token = payload['token']
        class_list = payload['list_of_subjects']
        try:
            user_data = jwt.decode(token, None, None)
            print(user_data['email'])
            response=json.dumps({'message': class_list})
            return HttpResponse(response, content_type='text/json')
        except Exception as e:
            response = json.dumps({'message': str(e)})
            return HttpResponse(response, content_type='text/json', status = 403)

@csrf_exempt
def add_class(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        token = payload['token']
        lessons_list = payload['list_of_lessons']
        try:
            user_data = jwt.decode(token, None, None)
            print(user_data['email'])
            response=json.dumps({'message': lessons_list})
            return HttpResponse(response, content_type='text/json')
        except Exception as e:
            response = json.dumps({'message': str(e)})
            return HttpResponse(response, content_type='text/json', status = 403)

    
        

    

