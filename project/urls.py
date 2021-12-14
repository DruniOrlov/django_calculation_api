"""project URL Configuration

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
from new_app.views import CalculationListOf10View, CalculationById, CalculationCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculation/get_last_10/', CalculationListOf10View.as_view(),),
    path('calculation/get_by_id/<int:id>/', CalculationById.as_view(),),
    path('calculation/create/', CalculationCreate.as_view(),),
]
