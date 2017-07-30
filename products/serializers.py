from rest_framework import serializers
from products.models import Product,ProductFeature

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'active', 'brand', 'categories')



    def create(self, validated_data):
        """
        Create and return a new `Products` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Products` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.save()
        return instance