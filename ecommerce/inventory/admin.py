from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Product, ProductType


class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("slug",)
    list_display = ("name", "slug", "is_active", "parent")
    search_fields = ("name",)


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("name", "slug", "category_link", "is_active", "seasonal_event")
    list_filter = ("stock_status",)
    list_display_links = ("name",)

    def category_link(self, obj):
        link = reverse("admin:inventory_category_change", args=[obj.category.id])
        # Create an HTML link
        return format_html(f'<a href="{link}">{obj.category.name}</a>')

    category_link.short_description = "Category"  # Optional: Set the column header


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    search_fields = ("name",)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
