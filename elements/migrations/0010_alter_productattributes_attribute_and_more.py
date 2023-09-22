# Generated by Django 4.2.5 on 2023-09-22 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0009_alter_product_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattributes',
            name='attribute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elements.attribute'),
        ),
        migrations.AlterField(
            model_name='productattributes',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elements.product'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elements.product'),
        ),
    ]
