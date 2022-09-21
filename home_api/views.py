from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Check, Task

@api_view(['get'])
def echo(request):
    return Response({'status': 'ok'})

@api_view(['post'])
def createUser(request):
    data = request.data
    
    if User.objects.filter(username=data.get('username')).exists():
        return Response({'status':'User exists'}, status=status.HTTP_208_ALREADY_REPORTED)

    user = User(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        username = data.get('username'),
        phone = data.get('phone')
    )
    user.save()
    return Response({'status':'created'}, status=status.HTTP_201_CREATED)