# Generated by Django 5.2.1 on 2025-05-28 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date_alter_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_url',
            new_name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(default='Resum per defecte'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.TextField(max_length=50),
        ),
    ]
