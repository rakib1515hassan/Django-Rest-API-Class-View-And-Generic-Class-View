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

## URL = ( http://127.0.0.1:8000/view-sets/viewsets/teacher-view-set/ )     দুইটি Url এখানে কাজ করবে।
## URL = ( http://127.0.0.1:8000/view-sets/viewsets/teacher-view-set/23/ )  দ্বিত্বয় টিতে শেষে id বসবে।
class TeacherViewSet(ViewSet):
    
    def list(self, request):
        tech = Teacher.objects.all()
        serializer = TeacherSerializer(tech, many = True)
        return Response(serializer.data)
    




    def retrieve(self, request, pk = None):
        id = pk
        if id is not None:
            try:
                tech = Teacher.objects.get(id = id)
                serializer = TeacherSerializer(tech)
                return Response(serializer.data)
            
            except Teacher.DoesNotExist:
                return Response( {'msg': 'This id is not found.'}, status= status.HTTP_404_NOT_FOUND)
            
    
    
    
    
    def create(self, request):
        serializer = TeacherSerializer( data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response( {'msg': 'Object is Created.'}, status= status.HTTP_201_CREATED )
        else:
            return Response( serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    




    def update(self, request, pk = None):
        id = pk
        if id is not None:
            try:
                tech = Teacher.objects.get(id = id)
                serializer = TeacherSerializer(tech, data= request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response( {'msg': 'Update suessfully compleate.'}, status= status.HTTP_200_OK )
                
                return Response( serializer.errors, {'msg': 'Update is not compleate.'}, status= status.HTTP_400_BAD_REQUEST)
            
            except Teacher.DoesNotExist:
                return Response( {'msg': 'Object Not Found.'}, status= status.HTTP_404_NOT_FOUND)
            

    


    def partial_update(self, request, pk = None):
        id = pk
        if id is not None:
            try:
                tech = Teacher.objects.get(id = id)
                serializer = TeacherSerializer(tech, data= request.data, partial = True)

                if serializer.is_valid():
                    serializer.save()
                    return Response( {'msg': 'Prtial Update suessfully compleate.'}, status= status.HTTP_200_OK )
                
                return Response( serializer.errors, {'msg': 'Partial Update is not compleate.'}, status= status.HTTP_400_BAD_REQUEST)
            
            except Teacher.DoesNotExist:
                return Response( {'msg': 'Object Not Found.'}, status= status.HTTP_404_NOT_FOUND)
        




    def destroy(self, request, pk = None):
        id = pk
        if id is not None:
            try:
                tech = Teacher.objects.get(id = id)
                tech.delete()
                return Response({'msg': 'Object suessfully Delete.'}, status= status.HTTP_200_OK)

            except Teacher.DoesNotExist:
                return Response( {'msg': 'Object Not Found.'}, status= status.HTTP_404_NOT_FOUND)

