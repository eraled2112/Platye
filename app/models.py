from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=123)
    image = models.ImageField(upload_to='image/categories/')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=123)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    description = models.TextField()
    price_rent = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']


class ProductImg(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='image/product/')


class Features(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=123)
    feature = models.CharField(max_length=123)

    def __str__(self):
        return f'{self.product} {self.title}'

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


