# Generated by Django 3.2.15 on 2022-08-09 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groceryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='Username',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
