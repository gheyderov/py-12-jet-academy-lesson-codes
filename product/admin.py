from django.contrib import admin
from product.models import ProductCategory, Product, ProductImage, ProductReview, ProductTag
from modeltranslation.admin import TranslationAdmin
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'category', 'quantity', 'get_tags', 'created_at']
    list_display_links = ['id', 'title']
    list_editable = ['category']
    # readonly_fields = ['price']
    list_filter = ['category', 'price']
    # list_per_page = 2
    search_fields = ['title', 'category__title']
    inlines = [ProductImageInline]

    def get_tags(self, obj):
        tags = []
        for tag in obj.tags.all():
            tags.append(tag.title)
        return tags


class ProductCategoryAdmin(TranslationAdmin):
    list_display = 'title',

admin.site.register(ProductCategory, ProductCategoryAdmin)

admin.site.register(ProductReview)
admin.site.register(ProductTag)

