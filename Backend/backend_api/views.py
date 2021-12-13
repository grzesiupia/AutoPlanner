"""
In this module, there are every endpoint functions.

All of them takes some Web request and return Web response.
"""
# pylint: disable=W0703, E1101, R1710, C0412, C0301
#from django.shortcuts import render
import json
from backend_api.models import Planners, Lessons, Teachers, Polls, Subjects, Classrooms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import send_mail
#from rest_framework_jwt.settings import api_settings
import jwt
from django.conf import settings


# Create your views here.

@csrf_exempt
def add_user(request):
    '''Function that takes user register request and returns response with the appropriate message,
     depending on whether the registration was successful  '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        username = payload['username']
        dbemail = payload['email']
        dbpassword = payload['password']
        user = Planners(login = username, password = dbpassword, planneremail = dbemail)
        try:
            user.save(force_insert = True)
            response = json.dumps({'Sukces': 'Pomyslnie dodano uzytkownika'})
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def get_user(request):
    '''Function that takes user login request and returns response with the appropriate message,
     depending on whether the login was successful. On success, it also returns a JWT token   '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        get_email = payload['email']
        get_password = payload['password']
        try:
            user = Planners.objects.get(planneremail=get_email, password=get_password)


            access_token_payload = {
            'email': user.planneremail,
            'login': user.login,
            'password': user.password
            }

            token = jwt.encode(access_token_payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')

            response = json.dumps({'userId': user.planneremail, 'accessToken': format(token)})
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json', status = 403)

@csrf_exempt
def add_subject(request):
    '''Function that takes new subject request and returns response with the appropriate message,
     depending on whether the addition of a subject was successful    '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['subject_name']
        token = payload['token']
        try:
            user_data = jwt.decode(token, None, None)
            subject = Subjects(subjectname = name, planneremail = user_data["email"])
            subject.save(force_insert = True)
            response=json.dumps({'message': 'Pomyslnie dodano lekcje'})
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_teacher(request):
    '''Function that takes new teacher request and returns response with the appropriate message,
     depending on whether the addition of a teacher was successful    '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        email = payload['email']
        token = payload['token']
        subjects = payload['list_of_subjects']
        #sub_list = payload['list_of_subjects']
        try:
            user_data = jwt.decode(token, None, None)
            pref_list = json.dumps(subjects)
            teacher = Teachers(email, name, pref_list, user_data['email'])
            teacher.save(force_insert = True)
            response=json.dumps({'message': 'Pomyslnie dodano nauczyciela'})
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json', status = 403)

@csrf_exempt
def add_classroom(request):
    '''Function that takes new classroom request and returns response with the appropriate message,
     depending on whether the addition of a classroom was successful    '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        token = payload['token']
        subjects = payload['list_of_subjects']
        try:
            user_data = jwt.decode(token, None, None)
            pref_list = json.dumps(subjects)
            classroom = Classrooms(name, pref_list, user_data['email'])
            classroom.save(force_insert = True)
            response=json.dumps({'message': subjects})
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_class(request):
    '''Function that takes new class request and returns response with the appropriate message,
     depending on whether the addition of a class was successful    '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        token = payload['token']
        lessons_list = payload['list_of_lessons'] 
        try:
            user_data = jwt.decode(token, None, None)
            for i in lessons_list:
                print (i['name'])
                teacher = Teachers.objects.get(planneremail = user_data['email'], teachername = i['teacher'])
                lesson = Lessons(planneremail = user_data['email'], classname = name, lessonname = i['name'], teacheremail = teacher.teacheremail, lessoncount = i['number'])
                lesson.save(force_insert = True)
            response=json.dumps({'message': 'pomyślnie dodano jednostki lekcyjne'})
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json', status = 403)

@csrf_exempt
def get_subjects(request):
    ''' A function that returns a list of subjects for a given user  '''
    if request.method == 'GET':
        payload = request.headers.get('x-access-token')
        print(payload)
        try:
            user_data = jwt.decode(payload, None, None)
            array = Subjects.objects.filter(planneremail = user_data['email'])
            subjects_list = []
            for i in array:
                subjects_list.append({'subject_name': i.subjectname})
            print(subjects_list)
            response=json.dumps(subjects_list)
            #response.setHeader("Access-Control-Allow-Origin", "*")
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json')

@csrf_exempt
def get_teachers(request):
    ''' A function that returns a list of teachers for a given user  '''
    if request.method == 'GET':
        payload = request.headers.get('x-access-token')
        print(payload)
        try:
            user_data = jwt.decode(payload, None, None)
            array = Teachers.objects.filter(email = user_data['email'])
            print(user_data['email'])
            teacher_list = []
            for i in array:
                teacher_list.append({'surname': i.teacher_name})
            print(teacher_list)
            response=json.dumps(teacher_list)
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json')

@csrf_exempt
def get_classrooms(request):
    ''' A function that returns a list of classrooms for a given user  '''
    if request.method == 'GET':
        payload = request.headers.get('x-access-token')
        print(payload)
        try:
            user_data = jwt.decode(payload, None, None)
            array = Lessons.objects.filter(email = user_data['email'])
            print(user_data['email'])
            classroom_list = []
            for i in array:
                if i not in classroom_list:
                    classroom_list.append({'classroom': i.classroom})
            print(classroom_list)
            response=json.dumps(classroom_list)
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json')

@csrf_exempt
def get_classes(request):
    ''' A function that returns a list of classes for a given user  '''
    if request.method == 'GET':
        payload = request.headers.get('x-access-token')
        print(payload)
        try:
            user_data = jwt.decode(payload, None, None)
            array = Lessons.objects.filter(email = user_data['email'])
            print(user_data['email'])
            class_list = []
            for i in array:
                if i not in class_list:
                    class_list.append({'class': i.class_name})
            print(class_list)
            response=json.dumps(class_list)
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json')

@csrf_exempt
def send_email(request):
    ''' The function that sends e-mails to teachers with a link to the survey,
     returns the appropriate message depending on the success of sending the e-mails  '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        token = payload['token']
        try:
            user_data = jwt.decode(token, None, None)
            planner = Planners.objects.get(email = user_data['email'])
            teachers = Teachers.objects.filter(email = user_data['email'])
            teacher_mail_list = []
            for i in teachers:
                rows = Polls.objects.all().count()
                poll = Polls(pool_id = rows + 1, email = planner, teacher_email = i, teacher_pref = None)
                poll.save(force_insert = True)
                teacher_mail_list.append({'teacher_email': i.teacher_email})
                send_mail(
                    'Wypelnij ankiete!',
                    'Link do ankiety to:  http://localhost:8080/poll/' + str(rows + 1),
                    'plan@generator.pl',
                    [str(i.teacher_email)],
                ) 
            response = json.dumps(teacher_mail_list)
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_poll_data(request, poll_number):
    '''The function saves the survey filled by the user to the database and
     returns the appropriate message depending on the success of sending the survey '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        #print(payload['poll'])
        # response = json.dumps(payload)
        # return HttpResponse(response, content_type='text/json')
        try:
            poll = Polls.objects.get(pool_id = poll_number)
            poll.teacher_pref = payload
            poll.save()
            response = json.dumps({"message": "Pomyslnie wyslano ankiete"})
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json')

@csrf_exempt
def generate_plan(request):
    '''A function that sends all the necessary data to the generator '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        token = payload['token']
        try:
            user_data = jwt.decode(token, None, None)
            lessons_list = Lessons.objects.filter(email = user_data['email']).order_by().values('class_name').distinct()
            print(lessons_list)
            classes = {}
            for i in lessons_list:
                if i['class_name'] is not None:
                    timetable_data = {}
                    lessons = Lessons.objects.filter(email = user_data['email'], class_name = i['class_name'])
                    # print(lessons)
                    for j in lessons:
                        timetable_data[j.lesson_name] = [j.numbers_of_lesson, j.teacher_email, j.classroom]
                    classes[i['class_name']] = timetable_data
            print(classes)
            response = json.dumps({'message': 'OK'})
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json')

@csrf_exempt
def del_subject(request):
    '''Function that takes delete subject request and returns response with the appropriate message,
     depending on whether the removal of a subject was successful    '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['subject_name']
        token = payload['token']
        try:
            #rows = Lessons.objects.all().count()
            #print(rows)
            user_data = jwt.decode(token, None, None)
            #print(user_data['email'])
            planner = Planners.objects.get(email = user_data['email'])
            lesson = Lessons.objects.get(email = planner, lesson_name = name)
            lesson.delete()
            response=json.dumps({'message': 'Pomyslnie usunieto lekcje'})
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json')

@csrf_exempt
def del_teacher(request):
    '''Function that takes delete teacher request and returns response with the appropriate message,
     depending on whether the removal of a teacher was successful    '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        email = payload['email']
        token = payload['token']
        try:
            user_data = jwt.decode(token, None, None)
            #print(user_data['email'])
            teacher = Teachers.objects.get(teacher_email = email, email = user_data['email'])
            teacher.delete()
            response=json.dumps({'message': 'Pomyslnie usunieto nauczyciela'})
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json', status = 403)

@csrf_exempt
def del_classroom(request):
    '''Function that takes delete classroom request and returns response with the appropriate message,
     depending on whether the removal of a classroom was successful    '''
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        token = payload['token']
        try:
            user_data = jwt.decode(token, None, None)
            #print(user_data['email'])
            lessons = Lessons.objects.filter(email = user_data['email'], classroom = name)
            for i in lessons:
                i.classroom = None
                i.save()
            response=json.dumps({'message': lessons})
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json')

@csrf_exempt
def del_class(request):
    '''Function that takes delete class request and 
        returns response with the appropriate message'''
    if request.method == 'POST':
        payload = json.loads(request.body)
        name = payload['name']
        token = payload['token']
        try:
            user_data = jwt.decode(token, None, None)
            lessons = Lessons.objects.filter(email = user_data['email'], class_name = name)
            for i in lessons:
                i.class_name = None
                i.save()
            response=json.dumps({'message': lessons})
            return HttpResponse(response, content_type='text/json')
        except Exception as exc:
            response = json.dumps({'message': str(exc)})
            return HttpResponse(response, content_type='text/json', status = 403)

