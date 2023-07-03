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


## Filtering against the current user
class Filter_Book_by_Author(ListAPIView):
    # queryset = Book.objects.filter(authors__user__username = "rakib") ## ঐ সকল Book দেখাবে যার Author এর Username = rakib
    # queryset = Book.objects.all()                                    ## সব গুলো Data দেখাবে।
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(authors__user__username = self.request.user) # যেই user Login থাকবে তার Book গুলো দেখাবে।
        return queryset
    

## Filtering against the URL
class Filter_Book_by_Author_2(ListAPIView):                                 
    serializer_class = BookSerializer

    def get_queryset(self):
        # username = self.kwargs['username'] 
        username = self.kwargs.get('username', None) 

        if username is not None:
            queryset = Book.objects.filter(authors__user__username = username) 
            return queryset
        return super().get_queryset()
    


## Filtering against query parameters
class Filter_Book_by_Author_3(ListAPIView):                                 
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(authors__user__username = username)
        return queryset
        
