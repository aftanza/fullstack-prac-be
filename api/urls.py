from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"user", views.UserView)
router.register(r"listing", views.ListingView)
router.register(r"cart", views.CartView)
router.register(r"cartItem", views.CartItemView)
router.register(r"wishlist", views.WishlistView)
router.register(r"wishlistItem", views.WishlistItemView)

# router_edit = routers.DefaultRouter()
# router_edit.register(r"ucustomser", views.EDIT_UserView)
# router_edit.register(r"listing", views.EDIT_ListingView)
# router_edit.register(r"cart", views.EDIT_CartView)
# router_edit.register(r"cartItem", views.EDIT_CartItemView)
# router_edit.register(r"wishlist", views.EDIT_WishlistView)
# router_edit.register(r"wishlistItem", views.EDIT_WishlistItemView)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/auth", views.AuthView.as_view()),
    # path("edit/user/<uuid:pk>", views.EDIT_UserView.as_view()),
    # path("edit/listing/<uuid:pk>", views.EDIT_ListingView.as_view()),
    # path("edit/cart/<uuid:pk>", views.EDIT_CartView.as_view()),
    # path("edit/cartItem/<uuid:pk>", views.EDIT_CartItemView.as_view()),
    # path("edit/wishlist/<uuid:pk>", views.EDIT_WishlistView.as_view()),
    # path("edit/wishlistItem/<uuid:pk>", views.EDIT_WishlistItemView.as_view()),
    # path("auth/callback", views.AuthView.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
