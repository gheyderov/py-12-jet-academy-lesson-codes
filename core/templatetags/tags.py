from product.models import ProductCategory, Product
from django.template import Library
register = Library()

@register.simple_tag
def get_categories():
    return ProductCategory.objects.filter(parent = None)


@register.inclusion_tag('includes/similar-products.html')
def get_similar_products():
    products = Product.objects.all()[:3]
    context = {
        'products' : products
    }
    return context