from django.urls import path, include

from GenericAPI.views._mixins import (
    TeacherListModelMixin,
    TeacherCreateModelMixin,
    TeacherRetrieveModelMixin,
    TeacherUpdateModelMixin,
    TeacherDestroyModelMixin,

    TeacherListCreateModelMixin,
    TeacherRetrieveUpdateDestroyModelMixin,
)

from GenericAPI.views._concreate import (
    TeacherList,
    TeacherCreate,
    TeacherRetrieve,
    TeacherUpdate,
    TeacherDestroy,

    TeacherListCreate,
    TeacherRetrieveUpdate,
    TeacherRetrieveDestroy,
    TeacherRetrieveUpdateDestroy,
)


urlpatterns = [

    # Mixins View - ( http://127.0.0.1:8000/generic/ )
    path('tech-list-mixins/',     TeacherListModelMixin.as_view()),
    path('tech-create-mixins/',   TeacherCreateModelMixin.as_view()),
    path('tech-retrieve-mixins/<int:pk>/', TeacherRetrieveModelMixin.as_view()),
    path('tech-update-mixins/<int:pk>/',   TeacherUpdateModelMixin.as_view()),
    path('tech-destroy-mixins/<int:pk>/',  TeacherDestroyModelMixin.as_view()),

    path('tech-list-create-mixins/',  TeacherListCreateModelMixin.as_view()),
    path('tech-retrieve-update-destroy-mixins/<int:pk>/',  TeacherRetrieveUpdateDestroyModelMixin.as_view()),


    ## Concreate View - ( http://127.0.0.1:8000/generic/ )
    path('tech-list/',    TeacherList.as_view()),
    path('tech-create/',  TeacherCreate.as_view()),
    path('tech-retrieve/<int:pk>/',TeacherRetrieve.as_view()),
    path('tech-update/<int:pk>/',  TeacherUpdate.as_view()),
    path('tech-destroy/<int:pk>/', TeacherDestroy.as_view()),

    path('tech-list-create/', TeacherListCreate.as_view()),
    path('tech-retrieve-update/<int:pk>/',  TeacherRetrieveUpdate.as_view()),
    path('tech-retrieve-destroy/<int:pk>/', TeacherRetrieveDestroy.as_view()),

    path('tech-retrieve-dpdate-destroy/<int:pk>/', TeacherRetrieveUpdateDestroy.as_view()),




]
