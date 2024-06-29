from django.core.management.base import BaseCommand
from api.models import (
    User,
    Listing,
    Cart,
    CartItem,
    Wishlist,
    WishlistItem,
)
import os


class Command(BaseCommand):
    help = "Creates or updates dummy data"

    def handle(self, *args, **options):
        techSeller, homeSeller, etcSeller = create_dummy_users()
        create_dummy_listings(techSeller, homeSeller, etcSeller)
        self.stdout.write(
            self.style.SUCCESS("Successfully updated/created dummy data.")
        )
        # create_dummy_carts()
        # create_dummy_cart_items()
        # create_dummy_wishlist()
        # create_dummy_wishlist_items()


def create_dummy_users():
    techSeller, created = User.objects.update_or_create(
        id="9989123125233",
        defaults={"email": "techSeller@example.com", "name": "techSeller"},
    )
    homeSeller, created = User.objects.update_or_create(
        id="2349453609546",
        defaults={"email": "homeSeller@example.com", "name": "homeSeller"},
    )
    etcSeller, created = User.objects.update_or_create(
        id="3498573498525",
        defaults={"email": "etcSeller@example.com", "name": "etcSeller"},
    )
    return techSeller, homeSeller, etcSeller


def create_dummy_listings(techSeller, homeSeller, etcSeller):
    tech_items = [
        {
            "product_name": "Phone",
            "product_description": "High-end smartphone",
            "quantity": 22,
            "price": 299.48,
            "category": "Technology",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Laptop",
            "product_description": "Gaming laptop",
            "quantity": 10,
            "price": 1200.00,
            "category": "Technology",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Headphones",
            "product_description": "Noise-cancelling headphones",
            "quantity": 50,
            "price": 199.99,
            "category": "Technology",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Smartwatch",
            "product_description": "Fitness tracking smartwatch",
            "quantity": 35,
            "price": 149.99,
            "category": "Technology",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Tablet",
            "product_description": "High-resolution display tablet",
            "quantity": 25,
            "price": 499.99,
            "category": "Technology",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Camera",
            "product_description": "DSLR camera with lens",
            "quantity": 15,
            "price": 899.99,
            "category": "Technology",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Router",
            "product_description": "High-speed wireless router",
            "quantity": 40,
            "price": 89.99,
            "category": "Technology",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Monitor",
            "product_description": "4K Ultra HD monitor",
            "quantity": 12,
            "price": 349.99,
            "category": "Technology",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "External Hard Drive",
            "product_description": "2TB portable external hard drive",
            "quantity": 30,
            "price": 89.99,
            "category": "Technology",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Keyboard",
            "product_description": "Mechanical keyboard with RGB lighting",
            "quantity": 20,
            "price": 79.99,
            "category": "Technology",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
    ]
    home_items = [
        {
            "product_name": "Sofa",
            "product_description": "Comfortable leather sofa",
            "quantity": 5,
            "price": 799.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Dining Table",
            "product_description": "Wooden dining table",
            "quantity": 8,
            "price": 499.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Bed",
            "product_description": "King size bed",
            "quantity": 3,
            "price": 599.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Armchair",
            "product_description": "Stylish armchair",
            "quantity": 10,
            "price": 299.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Bookshelf",
            "product_description": "Spacious bookshelf",
            "quantity": 7,
            "price": 199.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Coffee Table",
            "product_description": "Modern coffee table",
            "quantity": 12,
            "price": 149.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Lamp",
            "product_description": "Decorative floor lamp",
            "quantity": 20,
            "price": 89.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Curtains",
            "product_description": "Elegant window curtains",
            "quantity": 15,
            "price": 59.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Rug",
            "product_description": "Soft area rug",
            "quantity": 10,
            "price": 129.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Mirror",
            "product_description": "Full-length mirror",
            "quantity": 5,
            "price": 99.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
    ]
    etc_items = [
        {
            "product_name": "Book 1",
            "product_description": "Interesting novel",
            "quantity": 30,
            "price": 9.99,
            "category": "Books",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Toy Car",
            "product_description": "Remote-controlled car",
            "quantity": 15,
            "price": 29.99,
            "category": "Toys",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Watch",
            "product_description": "Stylish wrist watch",
            "quantity": 20,
            "price": 89.99,
            "category": "Accessories",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Board Game",
            "product_description": "Fun board game",
            "quantity": 25,
            "price": 19.99,
            "category": "Toys",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Sunglasses",
            "product_description": "Fashionable sunglasses",
            "quantity": 18,
            "price": 49.99,
            "category": "Accessories",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Backpack",
            "product_description": "Durable backpack",
            "quantity": 10,
            "price": 39.99,
            "category": "Accessories",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Water Bottle",
            "product_description": "Insulated water bottle",
            "quantity": 50,
            "price": 14.99,
            "category": "Sports & Outdoors",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Yoga Mat",
            "product_description": "Non-slip yoga mat",
            "quantity": 30,
            "price": 24.99,
            "category": "Sports & Outdoors",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Cookbook",
            "product_description": "Gourmet recipes cookbook",
            "quantity": 20,
            "price": 29.99,
            "category": "Books",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Umbrella",
            "product_description": "Windproof travel umbrella",
            "quantity": 40,
            "price": 19.99,
            "category": "Accessories",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Scarf",
            "product_description": "Warm winter scarf",
            "quantity": 25,
            "price": 15.99,
            "category": "Clothing",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Hat",
            "product_description": "Stylish fedora hat",
            "quantity": 10,
            "price": 25.99,
            "category": "Clothing",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Bluetooth Speaker",
            "product_description": "Portable Bluetooth speaker",
            "quantity": 15,
            "price": 59.99,
            "category": "Technology",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Notebook",
            "product_description": "Leather-bound notebook",
            "quantity": 35,
            "price": 12.99,
            "category": "Stationery",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Pen Set",
            "product_description": "Luxury pen set",
            "quantity": 20,
            "price": 29.99,
            "category": "Stationery",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Planner",
            "product_description": "2024 daily planner",
            "quantity": 40,
            "category": "Stationery",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Travel Mug",
            "product_description": "Stainless steel travel mug",
            "quantity": 25,
            "price": 14.99,
            "category": "Kitchen",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Cutlery Set",
            "product_description": "24-piece cutlery set",
            "quantity": 10,
            "price": 49.99,
            "category": "Kitchen",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Picture Frame",
            "product_description": "8x10 picture frame",
            "quantity": 30,
            "price": 14.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
        {
            "product_name": "Candle",
            "product_description": "Scented candle",
            "quantity": 50,
            "price": 9.99,
            "category": "Home & Living",
            "image_url": "https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png",
        },
    ]

    for tech_item in tech_items:
        listing, created = Listing.objects.update_or_create(
            product_name=tech_item["product_name"],
            user=techSeller,
            defaults={**tech_item, "user": techSeller},
        )

    for home_item in home_items:
        listing, created = Listing.objects.update_or_create(
            product_name=home_item["product_name"],
            user=homeSeller,
            defaults={**home_item, "user": homeSeller},
        )
    for etc_item in etc_items:
        listing, created = Listing.objects.update_or_create(
            product_name=etc_item["product_name"],
            user=etcSeller,
            defaults={**etc_item, "user": etcSeller},
        )
