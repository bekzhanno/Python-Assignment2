from django.db import models

# Create your models here.

class Product(models.Model):
    address = models.CharField(max_length=100, null=False, blank=False)
    balance = models.FloatField()



    def __str__(self):
        return f'{self.address} - {self.balance}'
        
