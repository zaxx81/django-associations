from django.db import models

# Create your models here.
class User(models.Model):
    pass


class Restaurant(models.Model):
    pass


class FoodItem(models.Model):
    pass


class Order(models.Model):
    # order.user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders") #user.orders
    # order.restaurant
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="orders") #restaurant.orders

    food_items = models.ManyToManyField(FoodItem, through="OrderFoodItem", related_name="orders")


class OrderFoodItem(models.Model):
    # order_food_item.order
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    # order_food_item.food_item
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE) 

    class Meta:
        unique_together = (("order", "food_item"))
