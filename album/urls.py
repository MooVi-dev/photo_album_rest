"""album URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from album import views

urlpatterns = [
    path("test/", views.HelloView.as_view(), name='hello'),
    path("album/", views.AlbumViewSet.as_view({'get': 'list'})),
    path("album/<int:pk>/", views.AlbumViewSet.as_view({'get': 'retrieve'})),
    path("add_album/", views.AlbumCreateViewSet.as_view({'post': 'create'})),
    path("update_album/<int:pk>/", views.AlbumCreateViewSet.as_view({'post': 'update'})),
    path("photo/", views.PhotoViewSet.as_view({'get': 'list'})),
    path("photo/<int:pk>/", views.PhotoViewSet.as_view({'get': 'retrieve'})),
    path("add_photo/", views.PhotoCreateViewSet.as_view({'post': 'create'})),
    path("update_photo/", views.PhotoCreateViewSet.as_view({'post': 'update'})),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
