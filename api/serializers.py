from rest_framework import serializers
from rest_framework.fields import CharField
from .models import (
    User,
    Listing,
    Cart,
    CartItem,
    Wishlist,
    WishlistItem,
    Auth,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]
        read_only_fields = ["created", "modified"]


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    # product_name = CharField(source="title", required=True)
    # product_description = CharField(source="description", required=True)

    class Meta:
        model = Listing
        fields = [
            "id",
            "product_name",
            "product_description",
            "quantity",
            "price",
            "category",
            "user",
            "created",
            "image_url",
            "modified",
        ]
        read_only_fields = ["id", "created", "modified"]


class CartSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = Cart
        fields = [
            "url",
            "id",
            "user",
            "created",
            "modified",
        ]
        read_only_fields = ["id", "created", "modified"]


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    cart = serializers.HyperlinkedRelatedField(view_name="cart-detail", read_only=True)
    product = serializers.HyperlinkedRelatedField(
        view_name="listing-detail", queryset=Listing.objects.all()
    )

    class Meta:
        model = CartItem
        fields = [
            "id",
            "cart",
            "product",
            "quantity",
            "created",
            "modified",
        ]
        read_only_fields = ["id", "created", "modified"]


class WishlistSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = Wishlist
        fields = [
            "id",
            "user",
            "created",
            "modified",
        ]
        read_only_fields = ["id", "created", "modified"]


class WishlistItemSerializer(serializers.HyperlinkedModelSerializer):
    wishlist = serializers.HyperlinkedRelatedField(
        view_name="wishlist-detail", read_only=True
    )
    product = serializers.HyperlinkedRelatedField(
        view_name="listing-detail", queryset=Listing.objects.all()
    )

    class Meta:
        model = WishlistItem
        fields = [
            "id",
            "wishlist",
            "product",
            "quantity",
            "created",
            "modified",
        ]
        read_only_fields = ["id", "created", "modified"]


class AuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auth
        fields = ["code", "scope", "authuser", "prompt"]


# class ModuleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Module
#         fields = ('id', 'title', 'description', 'video', 'test_bool', 'test_integer', 'created_at')
