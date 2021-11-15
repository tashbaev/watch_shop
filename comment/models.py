from django.db import models

from product.models import Product


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(verbose_name='Добавить отзыв:')
    # verified = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return f'{self.name} - {self.created}'

