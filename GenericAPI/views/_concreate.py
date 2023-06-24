from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import Student, Teacher
from app.serializers import StudentSerializer, TeacherSerializer
from django.views.decorators.csrf import csrf_exempt

# Function View
from rest_framework.decorators import api_view
# Class View
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,

    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,

    RetrieveUpdateDestroyAPIView,
)



# Create your views here.
class TeacherList(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class TeacherCreate(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class TeacherRetrieve(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class TeacherUpdate(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class TeacherDestroy(DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer





#------------------------------------------------------------------------

class TeacherListCreate(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class TeacherRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer




class TeacherRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class TeacherRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer