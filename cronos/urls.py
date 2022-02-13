"""cronos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from crud.views import home, form, create, view, edit, update, delete, servicos_home, servicos_form, servicos_create, servicos_view, servicos_edit, servicos_update, servicos_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('servicos_home/', servicos_home, name='servicos_home'),
    path('servicos_form/', servicos_form, name='servicos_form'),
    path('servicos_create/', servicos_create, name='servicos_create'),
    path('servicos_view/<int:pk>/', servicos_view, name='servicos_view'),
    path('servicos_edit/<int:pk>/', servicos_edit, name='servicos_edit'),
    path('servicos_update/<int:pk>/', servicos_update, name='servicos_update'),
    path('servicos_delete/<int:pk>/', servicos_delete, name='servicos_delete'),
]
