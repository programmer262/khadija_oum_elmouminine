# Generated by Django 3.1.1 on 2020-10-18 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('download', '0009_auto_20201018_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='présence',
            name='le_nom_du_la_personne_qui_écrit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
