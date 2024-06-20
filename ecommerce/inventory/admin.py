from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("slug",)
    list_display = ("name", "slug", "is_active", "parent")
    search_fields = ("name",)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
