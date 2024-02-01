from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserSerializer, UserRegisterSerializer
from .models import User


class UserRegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = UserRegisterSerializer

    @swagger_auto_schema(
        operation_description="Registration user",
        request_body=openapi.Schema(
            required=['full_name', 'phone_number',
                      'role', 'password', 'password2'],
            type=openapi.TYPE_OBJECT,
            properties={
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description="Phone number: as shown +998901234567"),
                'full_name': openapi.Schema(type=openapi.TYPE_STRING, description="Full name"),
                'role': openapi.Schema(type=openapi.TYPE_STRING, enum=['admin', 'waiter', 'customer'], description="Role"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            }
        )
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            token = Token.objects.get_or_create(user=user)[0].key
            response_data = {
                'token': token,
                'user': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
