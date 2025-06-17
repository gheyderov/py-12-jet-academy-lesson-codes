from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product, ProductCategory, ProductReview
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from product.forms import ReviewForm
from django.urls import reverse_lazy


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
    

class ProductDetailView(FormMixin, DetailView):
    template_name = 'shop-detail.html'
    model = Product
    form_class = ReviewForm
    # context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = ProductReview.objects.filter(product = self.get_object())
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            review = form.save(False)
            review.product = self.object
            review.user = self.request.user
            review.save()
            return redirect(reverse_lazy('shop-detail', kwargs = {'pk' : self.object.id}))



# def shop(request):
#     products = Product.objects.all() # select * from Product 
#     categories = ProductCategory.objects.all() # select * from ProductCategory
#     context = {
#         'products' : products,
#         'categories' : categories
#     }
#     return render(request, 'shop.html', context)

# def shop_detail(request, pk):
#     product = get_object_or_404(Product, pk = pk)
#     context = {
#         'product' : product
#     }
#     return render(request, 'shop-detail.html', context)