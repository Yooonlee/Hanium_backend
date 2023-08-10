from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .import views 


# router = DefaultRouter()
# router.register('upload', views.Uploader)


# urlpatterns = router.urls
# urlpatterns = [
#     path('upload/', views.Uploader),
#     path('',include(router.urls)),
# ]
urlpatterns = [
    # 형식 : collection이름/메서드/pk/추가정보
    path('diagnosis/image-upload', views.DiagnosisCreateAPIView.as_view(), name='diagnosis-image_upload'),
    # path('diagnosis/get/<int:pet_id>/list', views.DiagnosisListAPIView.as_view(), name='diagnosis-list'),
    # path('user/post/', views.UserCreateAPIView.as_view(), name='user-list'),
    # path('user/get/<int:user_id>', views.UserListAPIView.as_view(), name='user-detail'),

    path('user/create-user/', views.UserCreateView.as_view(), name='user-create_user'),    
    path('user/<int:user_id>/delete-user', views.UserDestroyView.as_view(), name='user-delete_user'),
    path('diagnosis/upload-diagnosis/', views.DiagnosisCreateView.as_view(), name='diagnosis-upload_diagnosis'),    
    path('pet/create-pet', views.PetCreateView.as_view(), name='pet-create_pet'),
    path('pet/<int:pet_id>/list-pet', views.PetRetrieveView.as_view(), name='pet-list_pet'),
    path('pet', views.PetListView.as_view(), name='pet-list_all'),
    path('pet/<int:pet_id>/delete-pet', views.PetDestroyView.as_view(), name='pet-delete_pet'),
    path('pet/update-pet/', views.PetUpdateView.as_view(), name='pet-update_pet'),

]
