import uuid
from django.shortcuts import render
from rest_framework import  status, parsers
from rest_framework.views import APIView
from .models import Diagnosis, Upload, Pet, User
from .serializers import DiagnosisSerializer, PetSerializer, UploadSerializer, UserSerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobClient
from datetime import datetime
from rest_framework.generics import get_object_or_404
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError
from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from django.http import Http404
import os, json
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
# swagger 
from rest_framework.views import APIView
from drf_yasg.utils       import swagger_auto_schema
from drf_yasg             import openapi 
from .serializers import *
##  ImageField Swagger에 표시
from rest_framework.decorators import parser_classes

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
    @swagger_auto_schema(request_body=GetDiagnosisUploadSerializer, responses={"201":GetResponseSerializer})

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
     # form data에서 pet_name, user_id 를 받아 컨테이너를 만들고  
     # form data에서 받은 image로 pet_name/업로드시간 으로 blob 이미지를 저장한다.
    @parser_classes((parsers.FormParser ,parsers.MultiPartParser, parsers.FileUploadParser))
    def post(self, request):
        
        # react에서 form data로 보내주면 아래와 같이 받음
        pet_name = request.POST['pet_name']
        users_id = request.POST['users_id']
        photo = request.FILES.__getitem__('photo')
        

        container_name =  str(users_id) + "-" + str(pet_name) + "-" + "photos"
        now = datetime.now()

        # 컨테이너 생성 
        try:
            container_client = ContainerClient.from_connection_string(conn_str= connectionString_blob, container_name=container_name)
            container_client.create_container()
        except ResourceExistsError:
            container_client = blob_client.get_container_client( container=container_name)
            print('A container with this name already exists')
    
        # blob 업로드
        
        file_upload_name = pet_name + now.strftime('%Y-%m-%d %H:%M')
        container_client.upload_blob(name=file_upload_name, data=photo, overwrite=True)
      
        response = {'message' : 'Creating Blob Success'}
        return Response(response, status=status.HTTP_201_CREATED)
        

class UserCreateView(APIView):
    @swagger_auto_schema(request_body=GetUserCreateSerializer, responses={"201":GetResponseSerializer})
    def post(self, request):
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            # collection_user.insert(user_serializer.data)
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 해당 속성값만 가져옴
class UserRetrieveView(APIView):
    @swagger_auto_schema(query_serializer=GetUserRequestSerializer, responses={"200":GetUserResponseManySerializer})
    def get(self, request, users_id):
        user = User.objects.all()
        User_Serializer = UserSerializer(user, many=True)
        try: 
            user = user.filter(users_id__icontains=users_id)
            User_Serializer = UserSerializer(user, many=True)
        except:
            return JsonResponse(User_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # UserSerializer = UserSerializer(user, many=True)
        
        return JsonResponse(User_Serializer.data, safe=False, status=status.HTTP_200_OK)
# 다 가져옴 
class UserListView(APIView):
    @swagger_auto_schema( responses={"200":GetUserResponseManySerializer})
    def get(self, request):
        user = User.objects.all()
        User_Serializer = UserSerializer(user, many=True) 
        return JsonResponse(User_Serializer.data, safe=False, status=status.HTTP_200_OK)


class UserDestroyView(APIView):
    @swagger_auto_schema(query_serializer=GetUserRequestSerializer, responses={"204":GetResponseSerializer})
    def get(self, request, users_id):
        user = User.objects.all()
        user = user.filter(users_id__icontains=users_id)
        user.delete()
        # pet.delete_many({"id" : users_id})
        # collection_user.delete_one({"id" : users_id})
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
class UserUpdateView(APIView):
    @swagger_auto_schema(request_body=GetUserUpdateRequestSerializer, responses={"200":GetResponseSerializer})
    def post(self, request, users_id):
        user = User.objects.get(users_id = users_id)
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = UserSerializer(user, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse({'message': tutorial_serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
class DiagnosisCreateView(APIView):
    @swagger_auto_schema(request_body=GetDiagnosisCreateSerializer, responses={"201":GetResponseSerializer})
    def post(self, request):
        diag_data = JSONParser().parse(request)
        diagnosis_serializer = DiagnosisSerializer(data=diag_data)
        if diagnosis_serializer.is_valid():
            diagnosis_serializer.save()
            # collection_diagnosis.insert(diagnosis_serializer.data)
            return JsonResponse(diagnosis_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(diagnosis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 해당 속성값만 가져옴
class DiagnosisRetrieveView(APIView):
    @swagger_auto_schema(query_serializer=GetDiagnosisRequestSerializer, responses={"200":GetDiagnosisResponseManySerializer})
    def get(self, request,pet_name):
        diagnosis = Diagnosis.objects.all()
        diagnosis = diagnosis.filter(pet_name__petname__icontains=pet_name)
        Diagnosis_Serializer = DiagnosisSerializer(diagnosis, many=True)
        
        return JsonResponse( Diagnosis_Serializer.data, safe=False, status=status.HTTP_200_OK)
# 다 가져옴 
class DiagnosisListView(APIView):
    @swagger_auto_schema( responses={"200":GetDiagnosisResponseManySerializer})
    def get(self, request):
        diagnosis = Diagnosis.objects.all()
        Diagnosis_Serializer = DiagnosisSerializer(diagnosis, many=True) 
        return JsonResponse(Diagnosis_Serializer.data, safe=False, status=status.HTTP_200_OK)


class PetCreateView(APIView):
    @swagger_auto_schema(request_body=GetPetCreateSerializer, responses={"201":GetResponseSerializer})
    def post(self, request):
        pet_data = JSONParser().parse(request)
        pet_serializer = PetSerializer(data=pet_data)
        
        if pet_serializer.is_valid():
            pet_serializer.save()
            # collection_pet.insert(pet_serializer.data)
            return JsonResponse(pet_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 해당 속성값만 가져옴
class PetRetrieveView(APIView):
    @swagger_auto_schema(query_serializer=GetPetRequestSerializer, responses={"200":GetPetResponseManySerializer})
    def get(self, request, petname):
        pet = Pet.objects.all()
        
        pet = pet.filter(petname__icontains=petname)
        Pet_Serializer = PetSerializer(pet, many=True)
        # Pet_Serializer = PetSerializer(pet, many=True)
        
        return JsonResponse( Pet_Serializer.data, safe=False, status=status.HTTP_200_OK)
# 다 가져옴 
class PetListView(APIView):
    @swagger_auto_schema( responses={"200":GetPetResponseManySerializer})
    def get(self, request):
        pet = Pet.objects.all()
        Pet_Serializer = PetSerializer(pet, many=True) 
       
        return JsonResponse(Pet_Serializer.data, safe=False, status=status.HTTP_200_OK)
        

class PetDestroyView(APIView):
    @swagger_auto_schema(query_serializer=GetPetRequestSerializer, responses={"204":GetResponseSerializer})
    def get(self, request, petname):
        pet = Pet.objects.all()
        pet = pet.filter(petname__icontains=petname)
        pet.delete()
        # pet.delete_many({"petname" : petname})
        # collection_pet.delete_many({"id" : petname})
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)

    
class PetUpdateView(APIView):
    @swagger_auto_schema(request_body=GetPetUpdateRequestSerializer, responses={"200":GetResponseSerializer})
    def post(self,request, petname):
        pet = Pet.objects.get(petname = petname)
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = PetSerializer(pet, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse( status=status.HTTP_400_BAD_REQUEST) 