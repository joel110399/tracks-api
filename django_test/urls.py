from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from tracks.views import ArtistView, GenreView
from tracks.viewsets import TrackViewSet

router = routers.DefaultRouter()

router.register('track', TrackViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('artist/', ArtistView.as_view(), name='Artist'),
    path('genre/', GenreView.as_view(), name='Genre'),
    path('', include(router.urls)),
]