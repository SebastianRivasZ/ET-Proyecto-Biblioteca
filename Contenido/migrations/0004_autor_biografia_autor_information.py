# Generated by Django 5.0.6 on 2024-07-13 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contenido', '0003_libro_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='biografia',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autor',
            name='information',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]