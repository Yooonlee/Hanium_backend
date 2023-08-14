from rest_framework import serializers
from .models import Diagnosis, Pet, User

class DiagnosisSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = Diagnosis
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = User
        fields = '__all__'
        
class PetSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = Pet
        fields = '__all__'

class UploadSerializer(serializers.Serializer):
    # id = serializers.IntegerField()

    userList = UserSerializer(many=True)
    diagList = DiagnosisSerializer(many=True)
    
    
#### Swagger - GetSerailizer
class GetUserRequestSerializer(serializers.Serializer):
    users_id = serializers.CharField()

class GetUserCreateInnerDictSerializer(serializers.Serializer):
    phone = serializers.CharField()
    email = serializers.CharField()
    users_id = serializers.CharField()
    users_password = serializers.CharField()

class GetUserCreateSerializer(serializers.Serializer):
    user_data = GetUserCreateInnerDictSerializer(many=True)
    
class GetUserUpdateInnerDictSerializer(serializers.Serializer):
    users_id = serializers.CharField(help_text = "url querystring 으로 전송")
    phone = serializers.CharField()
    email = serializers.CharField()
    users_password = serializers.CharField()

class GetUserUpdateRequestSerializer(serializers.Serializer):
    # tutorial_data = serializers.ListField()
    tutorial_data = GetUserUpdateInnerDictSerializer(many=True)
    
class GetUserRequestSerializer(serializers.Serializer):
    users_id = serializers.CharField()

class GetUserInnerDictSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    phone = serializers.CharField()
    email = serializers.CharField()
    users_id = serializers.CharField()
    users_password = serializers.CharField()    
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
class GetUserResponseManySerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    tutorial_data = GetUserInnerDictSerializer(many=True)

class GetUserResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    tutorial_data = GetUserInnerDictSerializer()






class GetPetInnerDictSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    users_id = serializers.CharField()
    petname = serializers.CharField()
    petage = serializers.IntegerField()
    petgender = serializers.CharField()
    petcomment = serializers.CharField()
    status = serializers.CharField()    
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class GetPetCreateInnerDictSerializer(serializers.Serializer):
    users_id = serializers.CharField()
    petname = serializers.CharField()
    petage = serializers.IntegerField()
    petgender = serializers.CharField()
    petcomment = serializers.CharField()
    status = serializers.CharField()            
class GetPetUpdateInnerDictSerializer(serializers.Serializer):
    petname = serializers.CharField(help_text = "url querystring 으로 전송")
    users_id = serializers.CharField()
    petname = serializers.CharField()
    petage = serializers.IntegerField()
    petgender = serializers.CharField()
    petcomment = serializers.CharField()
    status = serializers.CharField()    

class GetPetCreateSerializer(serializers.Serializer):
    pet_data = GetPetCreateInnerDictSerializer(many=True)

class GetPetRequestSerializer(serializers.Serializer):
    petname = serializers.CharField()

class GetPetUpdateRequestSerializer(serializers.Serializer):
    # tutorial_data = serializers.ListField()
    tutorial_data = GetPetUpdateInnerDictSerializer(many=True)
    
class GetResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()

class GetPetResponseManySerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    tutorial_data = GetPetInnerDictSerializer(many=True)

class GetPetResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    tutorial_data = GetPetInnerDictSerializer()





class GetDiagnosisUpdateInnerDictSerializer(serializers.Serializer):
    pet_name = serializers.CharField()
    petresult = serializers.CharField()
    petresultper = serializers.FloatField()
    diagday = serializers.TimeField()
    photo = serializers.ImageField()
    
class GetDiagnosisCreateSerializer(serializers.Serializer):
    pet_data = GetDiagnosisUpdateInnerDictSerializer(many=True)

class GetDiagnosisUploadSerializer(serializers.Serializer):
    pet_name = serializers.CharField()
    users_id = serializers.CharField()
    photo = serializers.ImageField()


class GetDiagnosisInnerDictSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    pet_name = serializers.CharField()
    petresult = serializers.CharField()
    petresultper = serializers.FloatField()
    diagday = serializers.TimeField()
    photo = serializers.ImageField()    
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class GetDiagnosisResponseManySerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    tutorial_data = GetDiagnosisInnerDictSerializer(many=True)

class GetDiagnosisResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    tutorial_data = GetDiagnosisInnerDictSerializer()

class GetDiagnosisRequestSerializer(serializers.Serializer):
    pet_name = serializers.CharField()
    
