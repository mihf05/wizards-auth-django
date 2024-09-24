from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import APIKey
import secrets
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save the new user
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    from django.contrib.auth import authenticate, login
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_route(request):
    return Response({'message': 'This is a protected route.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_api_key(request):
    new_key = secrets.token_urlsafe(32)
    api_key = APIKey.objects.create(user=request.user, key=new_key)
    return Response({'api_key': api_key.key}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_api_keys(request):
    api_keys = APIKey.objects.filter(user=request.user, is_active=True)
    return Response({'api_keys': [{'key': key.key, 'created_at': key.created_at} for key in api_keys]})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deactivate_api_key(request):
    key = request.data.get('key')
    try:
        api_key = APIKey.objects.get(user=request.user, key=key, is_active=True)
        api_key.is_active = False
        api_key.save()
        return Response({'message': 'API key deactivated successfully'}, status=status.HTTP_200_OK)
    except APIKey.DoesNotExist:
        return Response({'error': 'API key not found or already deactivated'}, status=status.HTTP_404_NOT_FOUND)
