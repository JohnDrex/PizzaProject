# Generated by Django 3.2 on 2022-12-12 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0006_alter_comments_pizza_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
