from rest_framework import serializers
from product.models import ProductCategory, Product, ProductTag


class ProductTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTag
        fields = [
            'title'
        ]


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = [
            'parent',
            'id',
            'title'
        ]


class ProductSerializer(serializers.ModelSerializer):

    # category = serializers.CharField(source = 'category.title')
    category = ProductCategorySerializer()
    tags = ProductTagSerializer(many = True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'category',
            'tags',
            'description',
            'cover_image',
            'quantity',
            'price',
            'slug'
        ]