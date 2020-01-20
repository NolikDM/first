from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

import os


@api_view(('GET',))
def index(request):
    workDir = os.path.dirname(os.path.realpath(__file__))               # возвращаем текущий рабочий каталог
    queDir = workDir + request.path                            
    os.chdir(queDir)                                         
    return(Response(os.listdir(path = '.')))                  

@api_view(('GET',))
def download(request):                                                  # метод удаленного скачивания файлов 
    workDir = os.path.dirname(os.path.realpath(__file__))
    queDir = workDir + request.path
    length = len(queDir)
    fName = request.GET.get("name")
    newLength = queDir[0:length - 6]
    pFile = newLength + fName                              
    file = open(pFile,"r")
    response = HttpResponse(file,content_type = 'application/msword')   
    response['Content-Disposition'] ='attachment; filename=' + fName   
    return response

@api_view(('GET',))
def create(request):                                                    # метод создания новой папки
    dirName = request.GET.get("name")                                   # получение параметров из строки запроса
    workDir = os.path.dirname(os.path.realpath(__file__))        
    queDir = workDir + request.path                                
    length = len(queDir)
    newLength = queDir[0:length - 6]
    os.mkdir(newLength + dirName)                                       # создаем новую директорию                         
    return(Response(os.listdir(path = '.')))               

@api_view(('GET',))
def delete(request):                                                    # метод удаления папки
    dirName = request.GET.get("name")
    workDir = os.path.dirname(os.path.realpath(__file__))    
    queDir = workDir + request.path                           
    length = len(queDir)
    newLength = queDir[0:length - 7]
    os.rmdir(newLength + dirName)                                       # удаляем пустую директорию                          
    return(Response(os.listdir(path = '.')))
