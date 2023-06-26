from django.urls import path, include

from ViewSets.views._ViewSets import (
    TeacherViewSet
)

from rest_framework.routers import DefaultRouter



# Creating Router Object
router = DefaultRouter()

# Router Registration StudentViewSet With Router
router.register('teacher-view-set', TeacherViewSet, basename='Teacher_ViewSets')


## URL = ( http://127.0.0.1:8000/view-sets/viewsets/teacher-view-set/ )
urlpatterns = [
    path('viewsets/', include(router.urls)),
]