from django.db import models

# Create your models here.

class Product(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class HistoricalData(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,db_column='ticker_id')
    timestamp = models.DateTimeField()
    open = models.DecimalField(max_digits=20, decimal_places=10)
    high = models.DecimalField(max_digits=20, decimal_places=10)
    low = models.DecimalField(max_digits=20, decimal_places=10)
    close = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return f'{self.product.name} - {self.timestamp}'
