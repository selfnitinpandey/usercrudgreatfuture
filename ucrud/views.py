from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
# Create your views here.
# show user
def user_get(request):
    username=User.objects.all()
    return render(request,'home.html',{'username':username})

# registeruser
def user_post(request):
    if request.method=='GET':
        return render(request,'add_user.html')
    else:
        username=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(username,firstname,lastname,email,password)
        user=User(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save()
        messages.success(request, 'User Has Been Registerd.')
        return HttpResponseRedirect('/')
# delete user

def user_delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    messages.success(request,'User Has Been Deleted.')
    return HttpResponseRedirect('/')

# edit user
def user_edit(request,id):
    if request.method=='POST':
        username=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(username,firstname,lastname,email,password)
        # u=User.objects.get(id=id)
        user=User(id=id,username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save()
        messages.success(request, 'User Has Been Updated..')
        return HttpResponseRedirect('/')
    else:
        username=User.objects.filter(id=id)
        return render(request,'update.html',{'username':username})

# Django rest framework

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status

@api_view(['GET', 'POST'])
def user(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def userged(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
