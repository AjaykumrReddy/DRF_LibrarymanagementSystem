"""librarymanagementsystem URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views as mainView
from admins import views as adminViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainView.index, name='index'),
    path('view_all_books/', mainView.view_all_books, name='view_all_books'),
    path('admin_register/', mainView.admin_register, name='admin_register'),
    path('admin_login/', mainView.admin_login, name='admin_login'),
    path('add_books/', adminViews.add_books, name='add_books'),
    path('view_books/', adminViews.view_books, name='view_books'),
    path('update_book/<str:pk>/', adminViews.update_book, name='update_book'),
    path('delete_book/<str:pk>/', adminViews.delete_book, name='delete_book'),
]
