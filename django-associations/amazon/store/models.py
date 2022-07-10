from django.db import models

# Create your models here.
class User(models.Model):
    pass


class Shop(models.Model):
    # shop.owner # should return a User
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="shop") # user.shop

    
class Product(models.Model):
    # product.shop
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products") # shop.products # products sold b
    

class Review(models.Model):
    # review.product
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews") # product.reviews
    
    # review.user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewed_products") # user.reviewed_products