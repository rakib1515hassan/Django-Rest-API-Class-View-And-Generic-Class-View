from app.models import Student, Teacher
from app.serializers import StudentSerializer, TeacherSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)



class TeacherListModelMixin( GenericAPIView, ListModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    





class TeacherCreateModelMixin( GenericAPIView, CreateModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)





class TeacherRetrieveModelMixin( GenericAPIView, RetrieveModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    


    

class TeacherUpdateModelMixin( GenericAPIView, UpdateModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    




class TeacherDestroyModelMixin( GenericAPIView, DestroyModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    



##----------------------------------------------------------------------------------------------

class TeacherListCreateModelMixin( GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class TeacherRetrieveUpdateDestroyModelMixin( GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)