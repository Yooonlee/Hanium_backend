from django.db import models

# auto_now=True : 수정 일자 = 최종 수정일자, django model이 save 될 때마다 현재날짜로 갱신됨! 
# auto_now_add=True : 생성일자, 갱신이 안됨, django model이 최초 저장 될때만 현재날짜를 저장함.
# Create your models here.

    
class User(models.Model):
    username = models.TextField(blank=True, unique=True)
    phone = models.TextField(blank=True)
    email = models.TextField(blank=True)
    user_id = models.TextField(blank=True)
    user_password = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True)
    
class Pet(models.Model):
    username = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True, db_column="username")
    petname = models.TextField(blank=True, unique=True)
    petage = models.TextField(blank=True)
    petgender = models.TextField(blank=True)
    petcomment = models.TextField(blank=True)
    status = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True)
    
class Diagnosis(models.Model):
    petname = models.ForeignKey('Pet', on_delete=models.CASCADE, blank=True, null=True, db_column="petname")
    petresult = models.TextField(blank=True)
    petresultper = models.TextField(blank=True)
    diagday = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True)
    
class Upload(models.Model):
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True)