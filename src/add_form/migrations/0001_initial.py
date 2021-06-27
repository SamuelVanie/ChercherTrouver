# Generated by Django 2.0.7 on 2021-06-27 22:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='add_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_objet', models.CharField(max_length=30)),
                ('date_de_trouvaille', models.DateTimeField()),
                ('description', models.TextField()),
                ('author', models.ForeignKey(default=None, on_delete=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
