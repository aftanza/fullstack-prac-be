from django.shortcuts import render
import time
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

import json

from .utils.google_auth import code_token_exchange, verify_id_token


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


class AuthView(views.APIView):
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            access_code = serializer.data["code"]

            print("access code: " + access_code)
            exchange_response = code_token_exchange(access_code)
            # access_token is a dictionary type

            # print(access_token)

            if "error" in exchange_response:
                print(f"Access token exchange error: {exchange_response['error']}")
                return Response(exchange_response, status=status.HTTP_400_BAD_REQUEST)

            # print("acess token: " + json.dumps(access_token))

            access_token = exchange_response["access_token"]
            refresh_token = exchange_response["refresh_token"]
            expires_in = exchange_response["expires_in"]
            id_token = exchange_response["id_token"]
            scope = exchange_response["scope"]

            time.sleep(1)

            # print(id_token)

            id_token_info = verify_id_token(id_token)
            if "error" in id_token_info:
                print(f"OpenID token error")
                return Response(id_token_info, status=status.HTTP_400_BAD_REQUEST)

            email = id_token_info["email"]
            id = id_token_info["id"]
            name = id_token_info["name"]
            print(email, name, id)

            user, created = User.objects.get_or_create(
                id=id, defaults={"email": email, "name": name}
            )
            if not created:
                user.email = email
                user.name = name
            # meaning that if data is already in the database
            user.save()

            # return Response(access_token, status=status.HTTP_201_CREATED)
            return Response(id_token_info, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------------------------------------------------------------------------------------------------------------------------------
# class EDIT_UserView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class EDIT_ListingView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer


# class EDIT_CartView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer


# class EDIT_CartItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer


# class EDIT_WishlistView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Wishlist.objects.all()
#     serializer_class = WishlistSerializer


# class EDIT_WishlistItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = WishlistItem.objects.all()
#     serializer_class = WishlistItemSerializer
