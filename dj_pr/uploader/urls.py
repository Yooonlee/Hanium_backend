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
    # collection이름/메서드/pk/추가정보
    path('diagnosis/post', views.DiagnosisCreateAPIView.as_view(), name='diagnosis-detail'),
    # path('diagnosis/get/<int:pet_id>/list', views.DiagnosisListAPIView.as_view(), name='diagnosis-list'),
    # path('user/post/', views.UserCreateAPIView.as_view(), name='user-list'),
    # path('user/get/<int:user_id>', views.UserListAPIView.as_view(), name='user-detail'),

    path('user/post/', views.UserCreateAPIView.as_view(), name='user-create'),    
    path('user/delete/<int:user_id>/', views.UserDestroyAPIView.as_view(), name='user-delete'),
    path('diagnosis/post/', views.DiagnosisCreateAPIView.as_view(), name='diagnosis-create'),    
    path('pet/post/', views.PetCreateAPIView.as_view(), name='pet-create'),
    path('pet/get/<int:pet_id>', views.PetRetrieveAPIView.as_view(), name='pet-retrieve'),
    path('pet/get/', views.PetListAPIView.as_view(), name='pet-list'),
    path('pet/delete/<int:pet_id>/', views.PetDestroyAPIView.as_view(), name='pet-delete'),
    path('pet/update/', views.PetUpdateAPIView.as_view(), name='pet-update'),

]
