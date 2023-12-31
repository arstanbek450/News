"""
URL configuration for News project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf import settings # !
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    # path('shorts/', shorts),  # To Do
    path('posts/<int:id>', post_detail),
    path('profile/<int:id>', profile_detail, name='profile'),
    path('shorts/', shorts, name='shorts-list'),
    path('short/<int:id>', short_info, name='shorts-info'),
    path('categories/', category_list, name='category-list'),
    path('categories/<int:id>/', category_detail, name='category-detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





