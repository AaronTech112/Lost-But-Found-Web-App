# Generated by Django 4.1.7 on 2023-11-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LbfApp', '0002_item_location_found'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('retrieved', 'retrieved'), ('missing', 'missing')], default='missing', max_length=100),
        ),
    ]