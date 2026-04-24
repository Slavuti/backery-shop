from django.db import models
from orders.models import Food 
from django.contrib.auth.models import User

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Basket for {self.user.username} | {self.food.Name}"

    # Этот метод считает сумму для одной позиции (цена * кол-во)
    def sum(self):
        return self.food.Price * self.quantity