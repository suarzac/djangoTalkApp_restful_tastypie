# Generated by Django 3.2.4 on 2021-06-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Talk', '0002_auto_20210604_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='duration',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
