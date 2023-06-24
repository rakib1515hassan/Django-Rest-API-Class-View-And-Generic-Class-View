from django.urls import path, include
from app.views import (
    TeacherApiView,
)

urlpatterns = [
    path('test-api-view/', TeacherApiView.as_view(), name='TeacherApiView'),
    path('test-api-view/<int:pk>/', TeacherApiView.as_view(), name='TeacherApiView'),
]
