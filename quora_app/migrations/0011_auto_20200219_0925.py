# Generated by Django 3.0.2 on 2020-02-19 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quora_app', '0010_auto_20200219_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
