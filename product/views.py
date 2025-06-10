from django.shortcuts import render, get_object_or_404
from product.models import Product, ProductCategory
from django.views.generic import ListView


# Create your views here.

class ProductListView(ListView):
    template_name = 'shop.html'
    model = Product # queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        cat_id = self.request.GET.get('category')
        if cat_id:
            queryset = queryset.filter(category = cat_id)
        return queryset


# def shop(request):
#     products = Product.objects.all() # select * from Product 
#     categories = ProductCategory.objects.all() # select * from ProductCategory
#     context = {
#         'products' : products,
#         'categories' : categories
#     }
#     return render(request, 'shop.html', context)

def shop_detail(request, pk):
    product = get_object_or_404(Product, pk = pk)
    context = {
        'product' : product
    }
    return render(request, 'shop-detail.html', context)