# Generated by Django 3.0.2 on 2020-02-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quora_app', '0003_auto_20200205_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(choices=[('U', 'Up Vote'), ('D', 'Down Vote'), ('no_act', 'no_act')], max_length=6),
        ),
    ]