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

    path('user/create-user', views.UserCreateView.as_view(), name='user-create_user'),    
    path('user/<str:users_id>/delete-user', views.UserDestroyView.as_view(), name='user-delete_user'),
    path('user/<str:users_id>/list-user', views.UserRetrieveView.as_view(), name='user-list_user'),
    path('user/', views.UserListView.as_view(), name='user-list_all'),
    path('user/<str:users_id>/update-user', views.UserUpdateView.as_view(), name='user-update_user'),
    path('diagnosis/upload-diagnosis', views.DiagnosisCreateView.as_view(), name='diagnosis-upload_diagnosis'),  
    path('diagnosis/<str:pet_name>/list-diagnosis', views.DiagnosisRetrieveView.as_view(), name='diagnosis-list_diagnosis'),
    path('diagnosis', views.DiagnosisListView.as_view(), name='diagnosis-list_all'),  
    path('pet/create-pet', views.PetCreateView.as_view(), name='pet-create_pet'),
    path('pet/<str:petname>/list-pet', views.PetRetrieveView.as_view(), name='pet-list_pet'),
    path('pet/', views.PetListView.as_view(), name='pet-list_all'),
    path('pet/<str:petname>/delete-pet', views.PetDestroyView.as_view(), name='pet-delete_pet'),
    path('pet/<str:petname>/update-pet', views.PetUpdateView.as_view(), name='pet-update_pet'),

]
