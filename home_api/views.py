from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Check, Task, Groups
import datetime

@api_view(['get'])
def echo(request):
    return Response({'status': 'ok'})

@api_view(['post'])
def createUser(request):
    data = request.data
    
    if User.objects.filter(username=data.get('username')).exists():
        return Response({'status':'User exists'}, status=status.HTTP_208_ALREADY_REPORTED)
    group = Groups.objects.get_or_create(group=data.get('group'))
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
    if reqeust.method == 'POST':
        data = reqeust.data
        for i in data:
            user = User.objects.get(username=i.get('username'))
            if Check.objects.filter(student=user, date=datetime.date.today()).exists():
                c = Check.objects.get(student=user, date=datetime.date.today())
                c.isHere = i.get('ishere')
            else:    
                c = Check(student=user, isHere=i.get('ishere'))
            c.save()
        return Response({'status': 'completed'}, status=status.HTTP_202_ACCEPTED)
    # Returns all user davomat todays
    users = User.objects.all()
    lst = []
    for user in users:
        dct = {}
        isHere = user.check_set.get(date=datetime.date.today()).isHere
        dct['full_name'] = user.full_name
        dct['ishere'] = isHere
        lst.append(dct)
    return Response({'status': 'good', 'data': lst}, status=status.HTTP_200_OK)
    
