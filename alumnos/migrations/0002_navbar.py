# Generated by Django 4.1.2 on 2024-06-29 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id_navbar', models.AutoField(db_column='idNavbar', primary_key=True, serialize=False)),
                ('nombre_nav', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]
