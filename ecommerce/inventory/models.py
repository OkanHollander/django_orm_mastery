import uuid

from django.db import models


# Create your models here.
class Product(models.Model):
    IN_STOCK = "IS"
    OUT_OF_STOCK = "OS"
    BACK_ORDER = "BO"

    STOCK_STATUS = [
        (IN_STOCK, "In Stock"),
        (OUT_OF_STOCK, "Out of Stock"),
        (BACK_ORDER, "Back Order"),
    ]

    pid = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(null=True)
    is_digital = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=False)
    stock_status = models.CharField(
        max_length=3,
        choices=STOCK_STATUS,
        default=OUT_OF_STOCK,
    )


class ProductLine(models.Model):
    price = models.DecimalField()
    sku = models.UUIDField(default=uuid.uuid4, editable=False)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField()
    weight = models.FloatField()


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    is_active = models.BooleanField(default=False)


class SeasonalEvents(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=100)
