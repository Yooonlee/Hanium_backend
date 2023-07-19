from rest_framework import serializers
from .models import Diagnosis, Pet, User

class DiagnosisSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Diagnosis
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = User
        fields = '__all__'
        
class PetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Pet
        fields = '__all__'

class UploadSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    userList = UserSerializer(many=True)
    diagList = DiagnosisSerializer(many=True)