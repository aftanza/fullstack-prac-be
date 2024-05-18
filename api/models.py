from django.db import models
from django_extensions.db.models import (
    TitleDescriptionModel,
    TimeStampedModel,
)
from .utils.model_abstracts import CustomIDModel


class Auth(models.Model):
    code = models.CharField(max_length=200)
    scope = models.CharField(max_length=200)
    authuser = models.CharField(max_length=200)
    prompt = models.CharField(max_length=200)


class User(TimeStampedModel):
    name = models.CharField(max_length=200)
    id = models.CharField(max_length=200, primary_key=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f"name: {self.name}, id: {self.id}"

    class Meta:
        ordering = ["created"]
        # verbose_name = "Learning Module"
        # verbose_name_plural = "Learning Modules"


class Listing(TitleDescriptionModel, TimeStampedModel, CustomIDModel):
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"Listing of {self.title} w/ quan {self.quantity} and price {self.price}"


class Cart(TimeStampedModel, CustomIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart for {self.user.name}"


class CartItem(TimeStampedModel, CustomIDModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Listing, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ["created"]


class Wishlist(TimeStampedModel, CustomIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wishlist for {self.user.name}"


class WishlistItem(TimeStampedModel, CustomIDModel):
    cart = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Listing, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ["created"]
