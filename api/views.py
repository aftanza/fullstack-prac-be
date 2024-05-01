from django.shortcuts import render
from rest_framework import viewsets, views, status, generics
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .serializers import (
    UserSerializer,
    ListingSerializer,
    CartSerializer,
    CartItemSerializer,
    WishlistSerializer,
    WishlistItemSerializer,
    AuthSerializer,
)
from .models import User, Listing, Cart, CartItem, Wishlist, WishlistItem, Auth

import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
GOOGLE_CLIENT_ID = str(os.getenv("GOOGLE_CLIENT_ID"))
GOOGLE_CLIENT_SECRET = str(os.getenv("GOOGLE_CLIENT_SECRET"))
GOOGLE_REDIRECT_URI = str(os.getenv("GOOGLE_REDIRECT_URI"))
GOOGLE_TOKEN_URI = str(os.getenv("GOOGLE_TOKEN_URI"))


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListingView(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class WishlistView(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class WishlistItemView(viewsets.ModelViewSet):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer


# --------------------------------------------------------------------------------------------------------------------------------------
class EDIT_UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EDIT_ListingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class EDIT_CartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class EDIT_CartItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class EDIT_WishlistView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class EDIT_WishlistItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer


class AuthView(views.APIView):
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser]

    def code_token_exchange(self, code):
        token_uri = GOOGLE_TOKEN_URI
        redirect_uri = GOOGLE_REDIRECT_URI
        client_id = GOOGLE_CLIENT_ID
        client_secret = GOOGLE_CLIENT_SECRET

        data = {
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        print(data)
        response = requests.post(token_uri, data=data, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else:
            error_message = (
                f"Got error during code_token_exchange. {response.status_code}"
            )
            # print(error_message)
            return {"error": error_message}

    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            access_code = serializer.data["code"]

            print("access code: " + access_code)
            access_token = self.code_token_exchange(access_code)

            # print(access_token)

            if "error" in access_token:
                print("acess token error: " + json.dumps(access_token))
                return Response(access_token, status=status.HTTP_400_BAD_REQUEST)

            # print("acess token: " + json.dumps(access_token))

            return Response(access_token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
