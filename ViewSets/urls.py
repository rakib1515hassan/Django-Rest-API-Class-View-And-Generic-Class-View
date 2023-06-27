from django.urls import path, include

from ViewSets.views._ViewSets import (
    TeacherViewSet
)
from ViewSets.views._ModelViewSets import (
    TeacherModelViewSet,
    TeacherReadOnlyModelViewSet,
)

from rest_framework.routers import DefaultRouter



# Creating Router Object
router = DefaultRouter()

# Router Registration StudentViewSet With Router
# ViewSet
router.register('teacher-view-set', TeacherViewSet, basename='Teacher_ViewSets')
# ModelViewSet
router.register('teacher-model-view-set', TeacherModelViewSet, basename='Teacher_Model_ViewSet')
# ReadOnlyModelViewSet
router.register('teacher-read-model-view-set', TeacherReadOnlyModelViewSet, basename='Read_Only_Model_ViewSet')


## http://127.0.0.1:8000/view-sets/viewsets/
## URL = ( http://127.0.0.1:8000/view-sets/viewsets/teacher-view-set/ )
## URL = ( http://127.0.0.1:8000/view-sets/viewsets/teacher-model-view-set/ )
## URL = ( http://127.0.0.1:8000/view-sets/viewsets/teacher-read-model-view-set/ )
urlpatterns = [
    path('viewsets/', include(router.urls)),
]