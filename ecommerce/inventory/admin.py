from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import (
    Attribute,
    AttributeValue,
    Category,
    Product,
    ProductImage,
    ProductLine,
    ProductType,
    SeasonalEvents,
)


class ChildCategoryInLine(admin.TabularInline):
    model = Category
    fk_name = "parent"
    extra = 1


class ChildProductTypeInLine(admin.TabularInline):
    model = ProductType
    fk_name = "parent"
    extra = 1


class ProductImageInLine(admin.StackedInline):
    model = ProductImage
    extra = 1


class ProductLineInLine(admin.StackedInline):
    model = ProductLine
    inlines = [ProductImageInLine]
    extra = 1


class AttributeValueInLine(admin.TabularInline):
    model = AttributeValue
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ChildCategoryInLine]
    readonly_fields = ("slug",)
    list_display = ("name", "slug", "is_active", "parent")
    search_fields = ("name",)

    def parent_name(self, obj):
        return obj.parent.name if obj.parent else "None"


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInLine]
    readonly_fields = ("slug",)
    list_display = (
        "name",
        "slug",
        "category_link",
        "is_active",
        "seasonal_event_link",
    )
    list_filter = ("stock_status",)
    list_display_links = ("name",)

    # Reverse lookup functions
    def category_link(self, obj):
        link = reverse("admin:inventory_category_change", args=[obj.category.id])
        # Create an HTML link
        return format_html(f'<a href="{link}">{obj.category.name}</a>')

    def seasonal_event_link(self, obj):
        try:
            link = reverse(
                "admin:inventory_seasonalevents_change", args=[obj.seasonal_event.id]
            )
            # Create an HTML link
            return format_html(f'<a href="{link}">{obj.seasonal_event.name}</a>')
        except AttributeError:
            return "None"

    category_link.short_description = "Category"
    seasonal_event_link.short_description = "Seasonal Event"


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    search_fields = ("name",)
    inlines = [ChildProductTypeInLine]


class AttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInLine]


class SeasonalEventsAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date")


class ProductLineAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "price",
        "sku",
        "stock_qty",
        "is_active",
        "order",
        "weight",
    )
    list_filter = ("is_active",)
    search_fields = ("product__name",)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        "product_line",
        "alternative_text",
        "url",
        "order",
    )
    list_filter = ("product_line",)
    search_fields = ("product_line__product__name",)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(SeasonalEvents, SeasonalEventsAdmin)
admin.site.register(ProductLine, ProductLineAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
