from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Diagnosis, Upload, Pet
from .serializers import UploadSerializer
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
import os
# 고객명에 해당하는 컨테이너를 만들고 그 안에 blob을 넣는 코드
# 컨테이너 명  = request.username
# blob(이미지 명) = request.petname/created_at

class DiagnosisCreateAPIView(APIView):
        
    def get_object(self, petname):
        try:
            return Pet.objects.filter(petname=petname)
        except Pet.DoesNotExist:
            raise Http404
     
    def get(self, request, petname,format=None):
        client = MongoClient('mongodb+srv://Yooonlee:Yooonlee@boilerplate.eb2feiy.mongodb.net/')
        db = client.haniumcat
        Pet = Pet.get_object(petname)
        petname= Pet.petname
        username= Pet.username
        
        # 컨테이너 생성 
        def create_blob_container(self, blob_service_client: BlobServiceClient, container_name):
            
            
            try:
                container_client = blob_service_client.create_container(name=container_name)
            except ResourceExistsError:
                print('A container with this name already exists')
        create_blob_container(container_name = username)
        
        # blob 업로드
        def upload_blob_file(self, blob_service_client: BlobServiceClient, container_name: str):
            container_client = blob_service_client.get_container_client(container=container_name)
            
            file = request.FILES['file']
            now = datetime.now()
            file_upload_name = petname + "/" + now.strftime('%Y-%m-%d %H:%M:%S')
            
            # with open(file=os.path.join('filepath', 'filename'), mode="rb") as data:
            blob_client = container_client.upload_blob(name=file_upload_name, data=file, overwrite=True)
        upload_blob_file(container_name=username)
        
        response = {'message' : 'Creating Container Success'}
        return Response(response, status=status.HTTP_201_CREATED)
        
        # try:
        #     file = request.FILES['file']
        #     now = datetime.now()
        #     file_upload_name = request.petname + "/" + now.strftime('%Y-%m-%d %H:%M:%S')
        #     blob= BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=yooonlee0b79fa;AccountKey=bkMC4GNh75Fi8kA+i4G5MYNrEbdSb+ysk57BO8HtS7F2K67Y3DS7paI/ytKeTh0OI/t8Ch7A1dF9+AStsL0TyQ==;BlobEndpoint=https://yooonlee0b79fa.blob.core.windows.net/;FileEndpoint=https://yooonlee0b79fa.file.core.windows.net/;QueueEndpoint=https://yooonlee0b79fa.queue.core.windows.net/;TableEndpoint=https://yooonlee0b79fa.table.core.windows.net/",
        #                                             container_name=str(request.username), blob_name=str(file_upload_name))
        #     blob.upload_blob(file)

        #     response = {'message': 'Blob uploaded'}
        #     return Response(response, status=status.HTTP_200_OK)
        # except:
        #     response = {'message' : 'Creating Container Failed'}
        #     return Response(response, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
