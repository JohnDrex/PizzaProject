# Generated by Django 3.2 on 2022-12-12 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0005_rename_comment_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='pizza_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='pizzas.pizza'),
        ),
    ]
