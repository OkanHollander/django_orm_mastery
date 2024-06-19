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
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
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
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    seasonal_event = models.ForeignKey(
        "SeasonalEvents", on_delete=models.SET_NULL, null=True
    )
    product_type = models.ManyToManyField("ProductType", related_name="product_type")


class ProductLine(models.Model):
    price = models.DecimalField()
    sku = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField()
    weight = models.FloatField()
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    attribute = models.ManyToManyField("Attribute", related_name="attribute")


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField()
    product_line = models.ForeignKey("ProductLine", on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=False)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True)


class SeasonalEvents(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=100, unique=True)


class Attribute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)


class ProductType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
