from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import SignupSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status

class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            User.objects.create_user(username=username, password=password)

class SigninView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        else:
            return Response({"error": "Invalid credentials"}, status=400)
        
class SignoutView(APIView):
    def post(self, request):
        try:
            token_key = request.auth.key
            token = Token.objects.get(key=token_key)
            token.delete()
            return Response({"detail": "Token deleted successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
