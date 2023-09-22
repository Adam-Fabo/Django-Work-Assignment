from rest_framework import serializers
from elements.models import AttributeValue, AttributeName, Attribute, Product, ProductAttributes, Image, ProductImage, Catalog


class CustomModelSerializer(serializers.ModelSerializer):
    """ Custom serializer that allows to map field names """
    aliases = {}

    def to_representation(self, instance):
        # Map aliases when serializing
        data = super().to_representation(instance)
        for key in self.aliases: 
            try: 
                data[self.aliases[key]] = data[key]
                del data[key] 
            except: pass
        return data

    def to_internal_value(self, data):
        # Map aliases when de-serializing
        for key in self.aliases: 
            try:
                data[key] = data[self.aliases[key]]
                del data[self.aliases[key]]
            except: pass
        return super().to_internal_value(data)



class AttributeValueSerializer(CustomModelSerializer):
    aliases = {'hodnota': 'value'}
    class Meta:
        model = AttributeValue
        fields = ('id','value')


class AttributeNameSerializer(CustomModelSerializer):
    aliases = {'name': 'nazev', 'code': 'kod', 'show': 'zobrazit'}
    class Meta:
        model = AttributeName
        fields = ('id','name','code', 'show')


class AttributeSerializer(CustomModelSerializer):
    aliases = {'nazev_atributu_id': 'attribute_name', 'hodnota_atributu_id': 'attribute_value'}
    class Meta:
        model = Attribute
        fields = ('id', 'attribute_name', 'attribute_value')


class ProductSerializer(CustomModelSerializer):
    aliases = {'nazev': 'name', 'description': 'popis', 'cena': 'cost', 'mena': 'currency', 'published_on': 'published_on', 'is_published': 'is_published'}
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'cost', 'currency', 'published_on', 'is_published')


class ProductAttributesSerializer(CustomModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = ('id','product','attribute')


class ImageSerializer(CustomModelSerializer):
    aliases = {'nazev': 'name', 'obrazek': 'image'}
    class Meta:
        model = Image
        fields = ('id', 'name', 'image')


class ProductImageSerializer(CustomModelSerializer):
    aliases = {'nazev': 'name', 'produkt_id': 'product', 'obrazek_id': 'image_id'}
    class Meta:
        model = ProductImage
        fields = ('id','name','product','image_id')


class CatalogSerializer(CustomModelSerializer):
    aliases = {'nazev': 'name', 'obrazek_id': 'image'}
    class Meta:
        model = Catalog
        fields = ('id','name','image','products_ids','attributes_ids')


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