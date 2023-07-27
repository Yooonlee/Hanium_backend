import uuid
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Diagnosis, Upload, Pet, User
from .serializers import DiagnosisSerializer, PetSerializer, UploadSerializer, UserSerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobClient
from datetime import datetime
from rest_framework.generics import get_object_or_404
# from rest_framework.generics import CreateAPIView
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError
from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from django.http import Http404
from pymongo import MongoClient
import os, json
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.generics import DestroyAPIView

# pymongo를 이용해 mongodb에 연결하는 code
# from pymongo import MongoClient

# connection_string = "mongodb+srv://Yooonlee:Yooonlee@boilerplate.eb2feiy.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(connection_string)
# db = client.get_database('haniumcat')
# collection_user = db.get_collection('User')
# collection_pet = db.get_collection('Pet')
# collection_diagnosis = db.get_collection('Diagnosis')

# blob connection string 
from azure.storage.blob import BlobServiceClient , ContainerClient
connectionString_blob = "DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=yooonlee0b79fa;AccountKey=bkMC4GNh75Fi8kA+i4G5MYNrEbdSb+ysk57BO8HtS7F2K67Y3DS7paI/ytKeTh0OI/t8Ch7A1dF9+AStsL0TyQ==;BlobEndpoint=https://yooonlee0b79fa.blob.core.windows.net/;FileEndpoint=https://yooonlee0b79fa.file.core.windows.net/;QueueEndpoint=https://yooonlee0b79fa.queue.core.windows.net/;TableEndpoint=https://yooonlee0b79fa.table.core.windows.net/"
blob_client = BlobServiceClient.from_connection_string(conn_str=connectionString_blob)

# 고객명에 해당하는 컨테이너를 만들고 그 안에 blob을 넣는 코드
# 컨테이너 명  =  user_id + pet_id + 생성된 시간
# blob(이미지 명) = pet_id/업로드시간 

#APIView를 상속받음
class DiagnosisCreateAPIView(APIView):
    
    # 아래 code 폐기    
    #  pet_id에 해당하는 object를 찾는다.
    # def get_object(self, pet_id):
    #     # mongodb client 불러오기
    #     client = MongoClient('mongodb+srv://Yooonlee:Yooonlee@boilerplate.eb2feiy.mongodb.net/')
    #     # dbname 정의하기
    #     db = client.haniumcat # db = haniumcat
    #     try:
    #         return db.Pet.find_one(id=pet_id)
    #     except Pet.DoesNotExist:
    #         raise Http404
    
     # post 메서드를 override
     # form data에서 id(pet_id), user_id 를 받아 컨테이너를 만들고  
     # form data에서 받은 image로 id(pet_id)/업로드시간 으로 blob 이미지를 저장한다.
    def post(self, request):
        
        # react에서 form data로 보내주면 아래와 같이 받음
        pet_id = request.POST['id']
        user_id = request.POST['user_id']
        image = request.FILES.__getitem__('pet_image')
        
        now = datetime.now()
        container_name =  str(user_id) + "-" + str(pet_id) + "-" + str(now.strftime('%Y-%m-%d'))

        # 컨테이너 생성 
        try:
            container_client = ContainerClient.from_connection_string(conn_str= connectionString_blob, container_name=container_name)
            container_client.create_container()
        except ResourceExistsError:
            container_client = blob_client.get_container_client( container=container_name)
            print('A container with this name already exists')
    
        # blob 업로드
        file_upload_name = pet_id + now.strftime('%Y-%m-%d %H:%M:%S')
        container_client.upload_blob(name=file_upload_name, data=image, overwrite=True)
      
        response = {'message' : 'Creating Blob Success'}
        return Response(response, status=status.HTTP_201_CREATED)
        

class UserCreateView(View):
    def post(self, request):
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            # collection_user.insert(user_serializer.data)
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDestroyView(View):
    def get(self, request, user_id):
        user = User.objects.all()
        user = user.filter(id__icontains=user_id)
        user.delete()
        # pet.delete_many({"id" : user_id})
        # collection_user.delete_one({"id" : user_id})
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
class DiagnosisCreateView(View):
    def post(self, request):
        user_data = JSONParser().parse(request)
        diagnosis_serializer = DiagnosisSerializer(data=user_data)
        if diagnosis_serializer.is_valid():
            diagnosis_serializer.save()
            # collection_diagnosis.insert(diagnosis_serializer.data)
            return JsonResponse(diagnosis_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(diagnosis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PetCreateView(View):
    def post(self, request):
        pet_data = JSONParser().parse(request)
        pet_serializer = PetSerializer(data=pet_data)
        
        if pet_serializer.is_valid():
            pet_serializer.save()
            # collection_pet.insert(pet_serializer.data)
            return JsonResponse(pet_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 해당 속성값만 가져옴
class PetRetrieveView(View):
    def get(self, request, pet_id):
        pet = Pet.objects.all()
        
        # url에 넣은 pet_id 에 해당하는 데이터를 가져옴        
        pet = pet.filter(id__icontains=pet_id)
        
        Pet_Serializer = PetSerializer(pet, many=True)
        return JsonResponse(Pet_Serializer.data, safe=False)
# 다 가져옴 
class PetListView(View):
    def get(self, request):
        pet = Pet.objects.all()
        Pet_Serializer = PetSerializer(pet, many=True)
        
        # user_id 대신 다른 속성 넣을 수 있음 
        # request 에서 user_id 이라는  key의 데이터을 가져옴 
        # db에서 title의 값을 가진 데이터를 불러옴
        title = request.GET.get('user_id', None)
        if title is not None:
            pet = pet.filter(user_id__icontains=title)
            Pet_Serializer = PetSerializer(pet, many=True)
        
        return JsonResponse(Pet_Serializer.data, safe=False)
        

class PetDestroyView(View):
    def get(self, request, pet_id):
        pet = Pet.objects.all()
        pet = pet.filter(id__icontains=pet_id)
        pet.delete()
        # pet.delete_many({"id" : pet_id})
        # collection_pet.delete_many({"id" : pet_id})
        return JsonResponse({'message': 'Pet was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    
class PetUpdateView(View):
    def get(request, pk):
        pet = Pet.objects.get(pk = pk)
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = PetSerializer(pet, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 