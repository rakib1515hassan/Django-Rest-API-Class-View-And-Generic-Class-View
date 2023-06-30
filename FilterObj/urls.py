from django.urls import path
from FilterObj.views import _data
from FilterObj.views import _filter




### URL = ( http://127.0.0.1:8000/filtering/ )
urlpatterns = [
    path('user/', _data.UserListCreateAPIView.as_view()),
    path('user-update/<int:pk>/', _data.UserUpdateAPIView.as_view()),
    path('user-retrieve-destroy/<int:pk>/', _data.UserRetrieveDestroyAPIView.as_view()),

    path('author/', _data.AuthorListCreateAPIView.as_view()),
    path('author-modify/<int:pk>/', _data.AuthorRetrieveUpdateDestroyAPIView.as_view()),
    


    path('publisher/', _data.PublisherListCreateAPIView.as_view()),
    path('publisher-modify/<int:pk>/', _data.PublisherRetrieveUpdateDestroyAPIView.as_view()),

    path('book/', _data.BookListCreateAPIView.as_view()),
    path('book-modify/<int:pk>/', _data.BookRetrieveUpdateDestroyAPIView.as_view()),

    path('store/', _data.StoreListCreateAPIView.as_view()),
    path('store-modify/<int:pk>/', _data.StoreRetrieveUpdateDestroyAPIView.as_view()),
]
