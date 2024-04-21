from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from .serializer import (
    TicketSerializer,
    ShopSerializer,
    RegisterSerializer,
    UserSerializer,
)
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from .models import Ticket, Shop
from datetime import datetime


# Create your views here.
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        """
        A function that retrieves a queryset based on the query parameters.

        Parameters:
            - year: year to get tickets from
            - month: month to get tickets from

        Returns:
            queryset: a queryset of Ticket objects based on the request parameters
        """
        filters = {}
        try:
            year = int(self.request.query_params.get("year", 0))
            month = int(self.request.query_params.get("month", 0))
        except ValueError:
            year = (False,)
            month = False

        if year:
            filters["date__year"] = year
        if month:
            filters["date__month"] = month

        queryset = Ticket.objects.filter(**filters)

        return queryset


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
