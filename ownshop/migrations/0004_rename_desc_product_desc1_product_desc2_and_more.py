# Generated by Django 4.0.2 on 2023-08-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownshop', '0003_product_product_sub_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='desc1',
        ),
        migrations.AddField(
            model_name='product',
            name='desc2',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='product',
            name='desc3',
            field=models.CharField(default='', max_length=800),
        ),
    ]
