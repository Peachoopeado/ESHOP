from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class OilType(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    category = models.ForeignKey(Category, related_name='o_types', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип масла'
        verbose_name_plural = 'Тип масла'

    def __str__(self):
        return self.name


class Viscosity(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    category = models.ForeignKey(Category, related_name='visc', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Вязкость'
        verbose_name_plural = 'Вязкость'

    def __str__(self):
        return self.name


class Compound(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    category = models.ForeignKey(Category, related_name='comp', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Состав'
        verbose_name_plural = 'Состав'

    def __str__(self):
        return self.name


class Fuel(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    category = models.ForeignKey(Category, related_name='fu', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Топливо'
        verbose_name_plural = 'Топливо'

    def __str__(self):
        return self.name
class Transmission(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    category = models.ForeignKey(Category, related_name='trans', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип трансмиссии'
        verbose_name_plural = 'Тип трансмиссии'
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  # Отношение 'многие к одному'
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='shop/img/products', blank=True)
    oilType = models.ForeignKey(OilType, related_name='oilType', on_delete=models.CASCADE)
    viscosity = models.ForeignKey(Viscosity, related_name='viscosity', on_delete=models.CASCADE)
    compound = models.ForeignKey(Compound, related_name='compound', on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, related_name='fuel', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
