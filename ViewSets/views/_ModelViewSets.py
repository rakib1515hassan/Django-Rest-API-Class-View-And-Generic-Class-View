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


## Create your views here.

## URL = ( http://127.0.0.1:8000/view-sets/viewsets/teacher-model-view-set/ )   ## দুইটি এক সাথে কাজ করবে।
## URL = ( http://127.0.0.1:8000/view-sets/viewsets/teacher-model-view-set/25/ ) ## এখানে শেষে id বসবে।
class TeacherModelViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer




## URL = ( http://127.0.0.1:8000/view-sets/viewsets/teacher-read-model-view-set/ )
## URL = ( http://127.0.0.1:8000/view-sets/viewsets/teacher-read-model-view-set/23/ ) ## এখানে শেষে id বসবে।
## এর মাধ্যমে আমরা শুধু GET Method access করতে পারবো।
class TeacherReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer