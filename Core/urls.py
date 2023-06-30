from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('generic/', include('GenericAPI.urls')),
    path('view-sets/', include('ViewSets.urls')),
    path('filtering/', include('FilterObj.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)