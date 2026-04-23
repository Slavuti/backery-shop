from django.db import models
from django.conf import settings


class Food(models.Model):
    Name = models.CharField('Name', max_length=30)
    Сompound = models.CharField('Compound', max_length=100)
    Description = models.TextField('Description', max_length=200)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Weight = models.CharField('Weight', max_length=100)
    image = models.ImageField('Image', upload_to='foods/', blank=True, null=True)
    def __str__(self):
        return self.Name
    
#   def get_absolute_url(self):
        return f'/orders/{self.id}'
    


#payment tracking 4
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    stripe_payment_intent = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id}"
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'