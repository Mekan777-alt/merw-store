from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категория продуктов'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    quantity = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products_image', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.category} - {self.name}'
