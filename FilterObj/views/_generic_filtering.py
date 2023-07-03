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
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

# NOTE আমরা এইভাবেও Filter এর জন্যে Class Declare করে দিতে পারি তেবে এর জন্যে আমাদের filterset_fields এর পরিবর্তে
# filterset_class = class_name বলে দিতে হবে। 
class BookFilter(filters.FilterSet):
    pubdate__year = filters.NumberFilter(field_name='pubdate', lookup_expr='year')

    class Meta:
        model = Book
        fields = ['name', 'price', 'authors__user__username', 'authors__phone']





## URL = ( http://127.0.0.1:8000/filtering/django_filter1/?name=&price=&authors__user__username=&authors__phone= )
## যা আমরা filter করতে চাই তা = এর পর দিতে হবে। Example: /?name = Easy Python & authors__user__username = rakib
class Django_Filter_1(ListAPIView):    
    queryset = Book.objects.all()                             
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend]

    # এই ভাবে Filter করলে icontains, iexact autometically থাকে Deffien করা লাগেনা।
    filterset_fields = ['name', 'price', 'authors__user__username', 'authors__phone']

    # filterset_fields = {
    #     # 'name': ['exact'],
    #     # 'name': ['startswith', 'endswith'], # startswith এবং endswith: এটি কোনো ফিল্ডের মানটি সংশোধিত শুরু এবং শেষ অংশের সাথে মিল খাবে।

    #     # 'name': ['contains'],       # contains: এটি একটি ম্যাচিং করবে যখন ফিল্টার মানটি কোনো ফিল্ডের একটি সাবস্ট্রিং (substring)
    #                                   # হিসাবে থাকবে।    
    #                                   # উদাহরণস্বরূপ, 'authors__user__username': ['contains'] দিতে পারেন যদি আপনি কোনো 
    #                                   # অক্ষরের মাধ্যমে প্রতিষ্ঠিত ফিল্টার করতে চান।
                              
    #     'name': ['icontains'],        # এটি Case Sensitive না।

    #     # 'price': ['exact'],
    #     'price': ['gt', 'lt'],     # gt এবং lt: এটি বড়/বৃহত্তর এবং ছোট/অবমান্যতর মানগুলির জন্য ফিল্টার করবে। উদাহরণস্বরূপ,
    #                                  # 'price': ['gt', 'lt'] দিতে পারেন যদি আপনি একটি মূল্যায়নের মধ্যে অবমান্যতর এবং বৃহত্তর
    #                                  # মূল্যায়ন দর্শাতে চান।

    #     # 'price': ['in'],             # এটি মানগুলির একটি তালিকা দিয়ে ফিল্টার করবে যখন কোনো ফিল্টার মানটি তালিকার মধ্যে থাকবে।
    #                                  # উদাহরণস্বরূপ, 'price': ['in'] দিয়ে আপনি মূল্যায়ন দির্ঘসূত্রের একটি তালিকা

    #     # Filter by author name
    #     # 'authors__user__username': ['exact'], 
    #     'authors__user__username': ['iexact'],  # iexact: এটি অবশ্যই ক্যাস-সেনসিটিভ (case-insensitive) এক্সাক্ট ম্যাচিং করবে। 

    #     'authors__phone': ['exact'],            # Filter by author phone number

    #     #'pubdate__year': ['exact']             # year এবং month: এটি তারিখ ফিল্টারিং করতে ব্যবহার করা যায়। উদাহরণস্বরূপ, ব্যবহার করে 
    #                                             # আপনি কোনো নির্দিষ্ট বছরে প্রকাশিত বইগুলির জন্য ফিল্টার করতে পারেন।
    # }

    # filterset_class = BookFilter
    




## URL ( http://127.0.0.1:8000/filtering/django_filter2/?search= )
## যা আমরা Search করতে চাই তা /?search= এর পর দিতে হবে। তবে আমরা যদি search এর যায়গায় অন্য কিছু লিখতে চাই তবে
## setting.py তে REST_FRAMEWORK = { 'SEARCH_PARAM': 'abc' } লিখতে হবে তবে আমরা /?abc=rakib ভাবে search করতে পারবো।
class Django_Filter_2(ListAPIView):    
    queryset = Book.objects.all()                             
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^name', 'publisher__name', '=authors__user__first_name', '=authors__user__last_name']    
                                # '^name' Start With
                                # '=name' Exact Matches
                                # '@name' Full Text Search (Currently only supported Django's PostgreSQL backend.)
                                # '$name' Regex Search

    # search_fields = {
    #     'name': ['iexact'],

    #     'publisher__name': ['iexact'],

    #     # 'authors__user__username': ['iexact'],
    #     'authors__user__first_name': ['iexact'],
    #     'authors__user__last_name': ['iexact'],
    # }
































## NOTE Generic Filtering------------------------------------------------------------------------------------------------
"""

                                ++ Generic Filtering++

  -> REST framework also include support for generic filtering backends that allow you to easy construct complex searchs and filter.
    Generic filters can also present themselves as HTML controls in the browsable API and admin API.

                                ++ Django Filter Backend++
  
  -> The Django-filter library includes a DjangoFilterBackend class which supports highly customaizable field filtering for REST freamwork.
    
    1.) To use DjangoFilterBackend, first install django-filter

    >> pip install django-filter

    2.) Then add 'django_filters' to Django's INSTALLED_APPS:

    INSTALLED_APPS = [
        ...
        'django_filters',
        ...
    ]

    3.) You should now either add the filter backend to your settings:

    REST_FRAMEWORK = {
    
        'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']

    }

    4.) Or add the filter backend to an individual View or ViewSet.

    from django_filters.rest_framework import DjangoFilterBackend

    class UserListView(generics.ListAPIView):
        ...
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['item-1', 'item-2']

                                           
"""