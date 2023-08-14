import uuid
from django.db import models

# auto_now=True : 수정 일자 = 최종 수정일자, django model이 save 될 때마다 현재날짜로 갱신됨! 
# auto_now_add=True : 생성일자, 갱신이 안됨, django model이 최초 저장 될때만 현재날짜를 저장함.
# Create your models here.

    
class User(models.Model):
    # username = models.TextField(blank=True, unique=True)
    # aaaid = models.BigAutoField(primary_key=True)
    id = models.AutoField(primary_key=True)
    phone = models.TextField(blank=True)
    email = models.TextField(blank=True)
    users_id = models.TextField(blank=True, unique=True)
    users_password = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True)
    
class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    users_id = models.ForeignKey("User", to_field="users_id", on_delete=models.CASCADE, blank=True, null=True, db_column="users_id")
    petname = models.TextField(blank=True, unique=True)
    petage = models.TextField(blank=True)
    petgender = models.TextField(blank=True)
    petcomment = models.TextField(blank=True)
    status = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True)
    
class Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    pet_name = models.ForeignKey("Pet", to_field="petname",  on_delete=models.CASCADE, blank=True, null=True, db_column="pet_name")
    petresult = models.TextField(blank=True)
    petresultper = models.TextField(blank=True)
    diagday = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True)
    
class Upload(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True)