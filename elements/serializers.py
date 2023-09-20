from rest_framework import serializers
from elements.models import AttributeValue, AttributeName, Attribute, Product, ProductAttributes, Image, ProductImage, Catalog


class AttributeValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttributeValue
        fields = '__all__'


class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeName
        fields = '__all__' #['id','nazev','code', 'show']


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = '__all__'  


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'

def get_serializer(element_name):
    if element_name == "AttributeValue":
        return AttributeValueSerializer
    elif element_name == "AttributeName":
        return AttributeNameSerializer
    elif element_name == "Attribute":
        return AttributeSerializer
    elif element_name == "Product":
        return ProductSerializer
    elif element_name == "ProductAttributes":
        return ProductAttributesSerializer
    elif element_name == "Image":
        return ImageSerializer
    elif element_name == "ProductImage":
        return ProductImageSerializer
    elif element_name == "Catalog":
        return CatalogSerializer
    else:
        raise NameError("Unsupported element name")