# Generated by Django 4.1.2 on 2022-10-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
