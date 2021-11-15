from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(primary_key=True)
    # parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.title


class Product(models.Model):
    BAND_CHOICES = (
        ('metal', 'Metal'),
        ('leather', 'Leather'),
        ('silicone', 'Silicone')
    )

    name = models.CharField(max_length=155)
    band = models.CharField(choices=BAND_CHOICES, max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created = models.DateTimeField(auto_now_add=True)
    

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'product_id': self.pk})

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        return self.images.first()

class Image(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url


