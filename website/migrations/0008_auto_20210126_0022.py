# Generated by Django 3.1.5 on 2021-01-25 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20210124_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='due',
            name='query',
            field=models.DateField(blank=True, null=True),
        ),
    ]