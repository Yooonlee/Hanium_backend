from rest_framework import serializers
from .models import Diagnosis, Pet, User

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class UploadSerializer(serializers.Serializer):
    userList = UserSerializer(many=True)
    diagList = DiagnosisSerializer(many=True)