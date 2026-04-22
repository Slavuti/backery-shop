from django.db import models

class Food(models.Model):
    Name = models.CharField('Name', max_length=30)
    Сompound = models.CharField('Compound', max_length=100)
    Description = models.TextField('Compound', max_length=200)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
#   img

    def __str__(self):
        return self.Name
    
#   def get_absolute_url(self):
        return f'/orders/{self.id}'
    
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'