from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import LoginToken
from django.contrib.auth.models import User
import secrets

@api_view(['POST'])
def send_login_token(request):
    email = request.data.get('email')
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Generate a secure token
    token = secrets.token_urlsafe(32)

    # Save the token
    login_token = LoginToken.objects.create(user=user, token=token)

    # Send email with the token
    subject = 'Your Login Token'
    message = f'Your login token is: {token}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        return Response({'message': 'Login token sent successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        login_token.delete()  # Delete the token if email sending fails
        return Response({'error': 'Failed to send login token'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def verify_login_token(request):
    token = request.data.get('token')
    try:
        login_token = LoginToken.objects.get(token=token, is_active=True)
        if login_token.is_valid():
            user = login_token.user
            login_token.is_active = False
            login_token.save()
            # Here you would typically create and return a JWT token
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)
    except LoginToken.DoesNotExist:
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
