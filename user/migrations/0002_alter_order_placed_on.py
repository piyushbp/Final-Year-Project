# Generated by Django 3.2 on 2021-04-21 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='placed_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
