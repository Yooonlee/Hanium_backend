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
    path('post/<str:petname>', views.DiagnosisCreateAPIView.as_view(), name='diagnosis-list'),

]
