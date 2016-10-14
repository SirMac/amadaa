from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('product-category-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{}".format(self.name)

class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('product-type-list')

    def __str__(self):
        return "{}".format(self.name)

class UnitOfMeasurement(models.Model):
    unit = models.CharField(max_length=30, unique=True)

    def get_absolute_url(self):
        return reverse('uom-list')

    def __str__(self):
        return "%(self.unit)s"

class SellableItem(models.Model):
    name = models.CharField(max_length=100)
    internal_ref = models.CharField(max_length=100, default='', blank=True)
    item_type = models.ForeignKey(ProductType, default=0)
    category = models.ForeignKey(ProductCategory)
    description = RichTextField(blank=True, default='')

    def __str__(self):
        return "{}".format(self.name)

class Product(SellableItem):
    purchase_units_of_measurement = models.ManyToManyField(UnitOfMeasurement,
            related_name='purchase_uoms')
    sale_units_of_measurement = models.ManyToManyField(UnitOfMeasurement,
            related_name='sale_uoms')

    def get_absolute_url(self):
        return reverse('product-list')

    def __str__(self):
        return "{}".format(self.name)

