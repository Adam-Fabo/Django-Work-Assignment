from django.db import models

class AttributeValue(models.Model):
    value = models.CharField(max_length=50, blank=True)


class AttributeName(models.Model):
    name = models.CharField(max_length=50, blank=True)
    code = models.CharField(max_length=50, blank=True)
    show = models.BooleanField(default=False, blank=True)


class Attribute(models.Model):
    attribute_name = models.ForeignKey(AttributeName, on_delete=models.CASCADE, null=True, blank=True)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE, null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=500, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True)
    currency = models.CharField(max_length=10, blank=True)
    published_on = models.DateTimeField(auto_now_add=True, blank=True)
    is_published = models.BooleanField(default=False, blank=True)


class ProductAttributes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=True, blank=True)


class Image(models.Model):
    name = models.CharField(max_length=50, blank=True)
    image = models.URLField(blank=True)


class ProductImage(models.Model):
    name = models.CharField(max_length=50, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    image_id = models.ForeignKey(Image,  null=True, blank=True, on_delete=models.CASCADE)


class Catalog(models.Model):
    name = models.CharField(max_length=50, blank=True)
    image = models.ForeignKey(Image, null=True,  blank=True, on_delete=models.DO_NOTHING)
    products_ids = models.ManyToManyField(Product, blank=True)
    attributes_ids = models.ManyToManyField(Attribute, blank=True)


def get_model(model):
    if model == "AttributeValue":
        return AttributeValue
    elif model == "AttributeName":
        return AttributeName
    elif model == "Attribute":
        return Attribute
    elif model == "Product":
        return Product
    elif model == "ProductAttributes":
        return ProductAttributes
    elif model == "Image":
        return Image
    elif model == "ProductImage":
        return ProductImage
    elif model == "Catalog":
        return Catalog
    else:
        raise NameError("Wrong element name")