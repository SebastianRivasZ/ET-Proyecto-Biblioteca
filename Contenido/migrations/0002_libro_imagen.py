# Generated by Django 5.0.6 on 2024-07-12 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contenido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
