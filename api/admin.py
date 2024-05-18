from django.contrib import admin
from .models import Auth, User, Listing, Cart, CartItem, Wishlist, WishlistItem


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "created", "modified")
    search_fields = ("name", "id", "email")
    list_filter = ("created", "modified")


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "quantity",
        "price",
        "user",
        "created",
        "modified",
    )
    search_fields = ("title", "description", "user__name")
    list_filter = ("created", "modified")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created", "modified")
    search_fields = ("user__name",)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "product", "quantity", "created", "modified")
    search_fields = ("cart__user__name", "product__title")
    list_filter = ("created", "modified")


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created", "modified")
    search_fields = ("user__name",)


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "product", "quantity", "created", "modified")
    search_fields = ("cart__user__name", "product__title")
    list_filter = ("created", "modified")
