from django.db import models

from product.models import Product


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE, related_name='comments')
    email =models.EmailField(verbose_name='Почта')
    body = models.TextField(verbose_name='Описание')
    verified = models.BooleanField(blank=True, default=False)

