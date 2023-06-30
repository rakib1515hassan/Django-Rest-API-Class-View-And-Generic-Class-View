from FilterObj.models import Author, Publisher, Book, Store
from FilterObj.serializers import (
    AuthorSerializer, 
    UserSerializer, 
    UserUpdateSerializer, 
    PublisherSerializer, 
    BookSerializer, 
    StoreSerializer
)

from django.contrib.auth import get_user_model
User = get_user_model()

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

## -----------------------------------------( Author )-----------------------------------------------
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

##__________________________________________________________________________________________________


## -----------------------------------------( Publishar )-----------------------------------------------
class PublisherListCreateAPIView(ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

##__________________________________________________________________________________________________



## -----------------------------------------( Book )-----------------------------------------------
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

##__________________________________________________________________________________________________


## -----------------------------------------( Store )-----------------------------------------------
class StoreListCreateAPIView(ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

##__________________________________________________________________________________________________