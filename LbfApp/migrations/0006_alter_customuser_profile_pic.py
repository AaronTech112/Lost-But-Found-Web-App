# Generated by Django 4.1.7 on 2023-11-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LbfApp', '0005_alter_item_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to='img'),
        ),
    ]
