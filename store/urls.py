"""store URL Configuration

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
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from users.views import UserCreateAPIView

from products.views import (
    ProductAdminListCreateAPIView,
    ProductAdminRetrieveUpdateDestroyAPIView,
    ProductClientRetrieveAPIView,
    ProductClientListAPIView
)

from orders.views import (
    OrderAdminListAPIView,
    OrderClientListAPIView
)

urlpatterns = [
    path('api/user', TokenObtainPairView.as_view()),
    path('api/user/refresh', TokenRefreshView.as_view()),
    path('api/users/register', UserCreateAPIView.as_view()),

    path('api/products', ProductAdminListCreateAPIView.as_view()),
    path('api/products/<int:pk>', ProductAdminRetrieveUpdateDestroyAPIView.as_view()),
    path('api/client/products', ProductClientListAPIView.as_view()),
    path('api/client/products/<int:pk>', ProductClientRetrieveAPIView.as_view()),

    path('api/orders', OrderAdminListAPIView.as_view()),
    path('api/client/<int:pk>/orders', OrderClientListAPIView.as_view()),
]