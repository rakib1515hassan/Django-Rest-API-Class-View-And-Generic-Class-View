from django.shortcuts import render
from app.models import Student, Teacher
from app.serializers import StudentSerializer, TeacherSerializer


from rest_framework.viewsets import (
    ViewSet,
    ModelViewSet, 
    ReadOnlyModelViewSet
)
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
# class TeacherViewSet(ViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer