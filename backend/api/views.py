import re
from django.http import HttpResponseRedirect
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TechStackSerializer, TaskSerializer
from DRF_Base.models import MyAccountManager, TechStack, Task, User
from DRF_Base.validators import UserRegistrationValidation


@api_view(['POST', 'DELETE', 'PATCH'])
def edit_todos(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({"message": "The data was saved to the database"})

    if request.method == 'DELETE':
        data = JSONParser().parse(request)
        task = Task.objects.get(name=data['name'])
        task.delete()

    if request.method == 'PATCH':
        data = JSONParser().parse(request)

        task = Task.objects.get(name=data['name'])
        task.description = data['description']
        if data['new_name'] == '':
            task.delete()
        else:
            task.name = data['new_name']
            task.save()

    return Response({"message": "Fetch wasn't successful"})


@api_view(['POST', 'DELETE', 'PATCH'])
def edit_PL(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TechStackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        if data['name'].strip() in ['']:
            item = TechStack.objects.get(name=data['old_name'])
            item.delete()
        else:
            item = TechStack.objects.get(name=data['old_name'])
            item.name = data['name']
            item.save()

    return Response({"message": "The data was saved to the database"})


@api_view(['POST', 'GET'])
def return_users_PL(request):
    pl = TechStack.objects.all()
    serializer = TechStackSerializer(pl, many=True)
    return Response([serializer.data])


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        users_credentials = JSONParser().parse(request)

        validation = UserRegistrationValidation(users_credentials['username'],
                                                users_credentials['email'],
                                                users_credentials['password'],
                                                users_credentials['password2'])
        response_dict = validation.validate_and_register()

        return Response(response_dict)
