"""
URL configuration for audioStore project.

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
from audioStore import settings
from django.conf.urls.static import static
from audioStoreApp.views import create_memory, get_memories, modify_memory, delete_memory, delete_memories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_memory/',create_memory,name="create_memory"),
    path('get_memories/', get_memories, name="get_memories"),
    path('modify_memory/<int:id>/update', modify_memory, name="modify_memory"),
    path('delete_memory/<int:id>/',delete_memory,name="delete_memory"),
    path('delete_memories/', delete_memories, name="delete_memories"),
]





urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)