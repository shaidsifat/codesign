from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Palette, Favorite
from .serializers import PaletteSerializer, FavoriteSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib.auth.models import User

## Palettelist api
class PaletteList(generics.ListCreateAPIView):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

### Favoritelist api
class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

### User registration
class UserRegistration(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = User.objects.create_user(username=username, password=password)
            if user:
                return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

### User login
class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

## Color Search Name
class SearchColorName(APIView):
   def get(self,request):
    
        search_query = request.query_params.get('query')
        matching_palettes = Palette.objects.filter(name__icontains=search_query, is_public=True)
        serializer = PaletteSerializer(matching_palettes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
