"""
                                 ++++++ Generic Api View ++++++
         -- Attribute --    

This class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views.
Attributes


1) queryset - The queryset that should be used for returning objects from this view. Typically, you must either set this attribute, or override the get_queryset() method. If you are overriding a view method, it is important that you call get_queryset() instead of accessing this property directly, as queryset will get evaluated once, and those results will be cached for all subsequent requests.


2) serializer_class - The serializer class that should be used for validating and deserializing input, and for serializing output. Typically, you must either set this attribute, or override the get_serializer_class() method. এই Method এর মাধ্যমে বলে দিতে হয় কোন Serializer এর সাহায্যে আমরা data কে serialize করবো।


3) lookup_field - The model field that should be used to for performing object lookup of individual model instances. Defaults to 'pk'.
    urls.py যে আমরা url লিখি সেখানে আমরা শুধু কেবল pk এ লিখতে পারি, but আমরা যদি চাই সেখানে অন্য কিছু আথবা id লিখতে তবে এর মাধ্যেমে তা পারি।


4) lookup_url_kwarg - The URL keyword argument that should be used for object lookup. The URL conf should include a keyword argument corresponding to this value. If unset this defaults to using the same value as lookup_field.


5) pagination_class - The pagination class that should be used when paginating list results. Defaults to the same value as the DEFAULT_PAGINATION_CLASS setting, which is 'rest_framework.pagination.PageNumberPagination'. Setting pagination_class=None will disable pagination on this view.


6) filter backends - A list of filter backend classes that should be used for filtering the queryset. Defaults to the same value as the DEFAULT_FILTER_BACKENDS setting.




         -- Meheod -- 

1) get_queryset(self) - It returns the queryset that should be used for list views, and that should be used as the base for lookups in detail views. Defaults to returning the queryset specified by the queryset attribute.
This method should always be used rather than accessing self.queryset directly, as self.queryset gets evaluated only once, and those results are cached for all subsequent requests.


2) get_object(self) - It returns an object instance that should be used for detail views. Defaults to using the lookup_field parameter to filter the base queryset.


3)  get_serializer_class(self) - It returns the class that should be used for the serializer. Defaults to returning the serializer_class attribute.


4) get_serializer_context(self) - It returns a dictionary containing any extra context that should be supplied to the serializer. Defaults to including 'request', 'view' and 'format' keys.


5) get_serializer(self, instance=None, data=None, many=False, partial=False) - It returns a serializer instance.


6) get_paginated_response(self, data) - It returns a paginated style Response object.
paginate_queryset(self, queryset) - Paginate a queryset if required, either returning a page object, or None if pagination is not configured for this view.


7) paginate_queryset(self, queryset) - Paginate a queryset if required, either returning a page object, or None if pagination is not configured for this view.


8) filter_queryset(self, queryset) - Given a queryset, filter it with whichever filter backends are in use, returing a new queryset.


        -- Mixins --

One of the big wins of using class-based views is that it allows us to easily compose reusable bits of behaviour.

The create/retrieve/update/delete operations that we've been using so far are going to be pretty similar for any model-backed API views we create.

Those bits of common behaviour are implemented in REST framework's mixin classes.

The mixin classes provide the actions that are used to provide the basic view behavior.

Note that the mixin classes provide action methods rather than defining the handler methods, such as get() and post(), directly. This allows for more flexible
composition of behavior.


from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


1) ListModelMixin
2) CreateModelMixin
3) RetrieveModelMixin
4) UpdateModelMixin
5) DestroyModelMixin

""" 
