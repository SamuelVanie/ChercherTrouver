# Generated by Django 2.0.7 on 2021-07-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('take_form', '0005_auto_20210705_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='take_form',
            name='objet_id',
            field=models.IntegerField(default=None, null=True),
        ),
    ]