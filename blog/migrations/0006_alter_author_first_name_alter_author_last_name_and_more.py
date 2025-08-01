# Generated by Django 5.2.1 on 2025-05-28 16:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_tag_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(30)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(default='Resum per defecte', validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
