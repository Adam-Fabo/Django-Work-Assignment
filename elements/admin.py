from django.contrib import admin
from elements.models import AttributeValue, AttributeName, Attribute, Product, ProductAttributes, Image, ProductImage, Catalog


admin.site.register(AttributeValue)
admin.site.register(AttributeName)
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(ProductAttributes)
admin.site.register(Image)
admin.site.register(ProductImage)
admin.site.register(Catalog)