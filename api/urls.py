from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'tickets', views.TicketViewSet)
router.register(r'shops', views.ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]