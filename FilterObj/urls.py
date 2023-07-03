from django.urls import path, include
from FilterObj.views import _data
from FilterObj.views import _filter
from FilterObj.views import _generic_filtering




### URL = ( http://127.0.0.1:8000/filtering/ )
urlpatterns = [
    ## -------------------------( _data.py )---------------------------------------
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





    ## -------------------------( _filter.py )---------------------------------------
    path('filter-book-by-author/', _filter.Filter_Book_by_Author.as_view()),
    path('filter-book-by-author2/<str:username>/', _filter.Filter_Book_by_Author_2.as_view()),
    path('filter-book-by-author3/', _filter.Filter_Book_by_Author_3.as_view()),






    ## -------------------------( _generic_filter.py )-------------------------------
    path('django_filter1/', _generic_filtering.Django_Filter_1.as_view()),
    path('django_filter2/', _generic_filtering.Django_Filter_2.as_view()),





    #________________________________________________________________________________
    # For Session Authentication Weneed Login Form, That whay it are needed.
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
