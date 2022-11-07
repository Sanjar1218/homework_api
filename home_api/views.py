from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User, Group
from .models import Check, Task, HomeWork
import datetime

@api_view(['get'])
def echo(request):
    return Response({'status': 'ok'})

@api_view(['post'])
def homework(request):
    # in the future we gonna change this to serializers
    # getting data from reqeust
    data = request.data 
    github = data.get('github')
    repo = data.get('repo')
    tasks = data.get('tasks')

    user = User.objects.get(username=github)
    # it doesn't matter homework created or not
    base, created = HomeWork.objects.get_or_create(name=repo, user=user)
    for task in tasks:
        t, c = base.task.get_or_create(name=task.get('name'))
        # if not created it's gonna updateds attempt and isSolved attributes
        if not c:
            t.attempt +=1
            t.isSolved = task.get('isSolved')
            t.save()
    return Response({'status':'ok'}, status=status.HTTP_200_OK)


@api_view(['post'])
def createUser(request):
    data = request.data
    
    if User.objects.filter(username=data.get('username')).exists():
        return Response({'status':'User exists'}, status=status.HTTP_208_ALREADY_REPORTED)
    
    group, created = Group.objects.get_or_create(name=data.get('group'))
    user = User(
        first_name = data.get('first_name'),
        last_name  = data.get('last_name'),
        username   = data.get('username'),
        phone      = data.get('phone'),
        group      = group
    )
    user.save()
    return Response({'status':'created'}, status=status.HTTP_201_CREATED)

@api_view(['post', 'get'])
def davomat(reqeust):
    data = reqeust.data
    if reqeust.method == 'POST':
        for i in data:
            date = datetime.datetime.strptime(i.get('date'), '%d-%m-%y').date()
            user = User.objects.get(username=i.get('username'))
            if Check.objects.filter(student=user, date=date).exists():
                c = Check.objects.get(student=user, date=date)
                c.isHere = i.get('ishere')
            else:
                c = Check(student=user, isHere=i.get('ishere'), date=date)
            c.save()
        return Response({'status': 'completed'}, status=status.HTTP_202_ACCEPTED)
    # Returns all user davomat todays
    data = reqeust.headers
    print(data)
    users = Group.objects.get(group=data.get('group')).user_set.all()
    lst = []
    for user in users:
        dct = {}
        date = datetime.datetime.strptime(data.get('date'), '%d-%m-%y')
        if user.check_set.filter(date=date).exists():
            isHere = user.check_set.get(date=date).isHere
            dct['full_name'] = user.full_name
            dct['ishere'] = isHere
            lst.append(dct)
    return Response({'status': 'good', 'data': lst}, status=status.HTTP_200_OK)
    
