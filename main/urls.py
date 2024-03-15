from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  
from .views import TaskViewSet, VolunteerViewSet


urlpatterns = [

    path('api/task', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='task'),
    path('api/vol', VolunteerViewSet.as_view({'get': 'list', 'post': 'create'}), name='vol'),
#   path('api/doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
  

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from main.views import TaskViewSet

# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
