from django.http import JsonResponse
from product.models import ProductCategory, Product, ProductTag
from product.api.serializers import ProductCategorySerializer, ProductSerializer, ProductTagSerializer


def categories(request):
    category_list = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer(category_list, many = True)
    # category_dict = []
    # for category in category_list:
    #     if category.parent:
    #         category_dict.append({
    #             'parent': category.parent.id,
    #             'id' : category.id,
    #             'title' : category.title
    #         })
    #     else:
    #         category_dict.append({
    #             'id' : category.id,
    #             'title' : category.title
    #         })
    return JsonResponse(data = serializer_class.data, safe=False)


def products(request):
    product_list = Product.objects.all()
    serializer_class = ProductSerializer(product_list, context = {'request' : request}, many = True)
    return JsonResponse(data = serializer_class.data, safe = False)


def producttags(request):
    tags = ProductTag.objects.all()
    serializer_class = ProductTagSerializer(tags, many = True)
    return JsonResponse(data = serializer_class.data, safe = False)