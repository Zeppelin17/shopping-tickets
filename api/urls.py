from django.urls import path, include
from rest_framework import routers
from api import views

from knox import views as knox_views
from .views import  LoginAPI, RegisterAPI

router = routers.DefaultRouter()
router.register(r'tickets', views.TicketViewSet)
router.register(r'shops', views.ShopViewSet)

urlpatterns = [
    path('signup', RegisterAPI.as_view(), name='Sign Up'),
    path('login', LoginAPI.as_view(), name='Login'),
    path('logout', knox_views.LogoutView.as_view(), name='Logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='Logout All'),
    path('', include(router.urls)),
]