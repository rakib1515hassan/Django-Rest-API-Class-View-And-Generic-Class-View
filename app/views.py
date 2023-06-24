from django.shortcuts import render
from django.http import HttpResponse
from app.models import Student, Teacher
from app.serializers import StudentSerializer, TeacherSerializer

# Function View
from rest_framework.decorators import api_view
# Class View
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONOpenAPIRenderer, JSONRenderer

# Exception
from django.core.exceptions import ObjectDoesNotExist


class TeacherApiView(APIView):

    def get(self, request, pk = None, format=None):
        id = pk
        if id is not None:
            try:
                teacher = Teacher.objects.get(id = id)
                serializer = TeacherSerializer(teacher)
                return Response(serializer.data)
            except Teacher.DoesNotExist:
                return Response( {'msg': 'This id is not found.'} )

        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many = True)
        return Response( serializer.data, status= status.HTTP_200_OK )
    

    
    def post(self, request, format=None):
        serializer = TeacherSerializer( data = request.data )
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is successfully save in Database.'}
            return Response( {'res':res}, status= status.HTTP_200_OK)
        
        return Response( serializer.errors, status= status.HTTP_404_NOT_FOUND)
    


    def put(self, request, pk, format=None):
        id = pk
        try:
            teacher =Teacher.objects.get(id = id)
            serializer = TeacherSerializer( teacher,  data = request.data )
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data is successfully Update in Database.'}
                return Response( {'res':res}, status= status.HTTP_200_OK )
            
            return Response( serializer.errors, status= status.HTTP_404_NOT_FOUND )
        
        except Teacher.DoesNotExist:
                return Response( {'msg': 'This id is not found.'} )


    def patch(self, request, pk, format=None):
        id = pk
        try:
            teacher =Teacher.objects.get(id = id)
            serializer = TeacherSerializer( teacher,  data = request.data, partial = True )
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Partial Update in Database.'}
                return Response( {'res':res}, status= status.HTTP_200_OK )
            
            return Response( serializer.errors, status= status.HTTP_404_NOT_FOUND )
        
        except Teacher.DoesNotExist:
                return Response( {'msg': 'This id is not found.'} )



    def delete(self, request, pk, format=None):
        id = pk
        try:
            teacher =Teacher.objects.get(id = id)
            teacher.delete()
            res = {'msg': 'Data Successfully Deleted.'}
            return Response( {'res':res}, status= status.HTTP_200_OK )
        
        except Teacher.DoesNotExist:
                return Response( {'msg': 'This id is not found.'} )