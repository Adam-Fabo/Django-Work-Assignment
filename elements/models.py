from django.db import models

# Create your models here.

class AttributeValue(models.Model):
    hodnota = models.CharField(max_length=50, blank=True)


class AttributeName(models.Model):
    nazev = models.CharField(max_length=50, blank=True)
    kod = models.CharField(max_length=50, blank=True)
    zobrazit = models.BooleanField(default=False, blank=True)


class Attribute(models.Model):
    nazev_atributu_id = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    hodnota_atributu_id = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)


class Product(models.Model):
    nazev = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=500, blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    mena = models.CharField(max_length=10, blank=True)
    published_on = models.DateTimeField(auto_now_add=True, blank=True)
    is_published = models.BooleanField(default=False, blank=True)


class ProductAttributes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)


class Image(models.Model):
    nazev = models.CharField(max_length=50, blank=True)
    obrazek = models.URLField(blank=True)


class ProductImage(models.Model):
    nazev = models.CharField(max_length=50, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    obrazek_id = models.ForeignKey(Image,  null=True, blank=True, on_delete=models.CASCADE)


class Catalog(models.Model):
    nazev = models.CharField(max_length=50, blank=True)
    obrazek_id = models.ForeignKey(Image, null=True,  blank=True, on_delete=models.DO_NOTHING)
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