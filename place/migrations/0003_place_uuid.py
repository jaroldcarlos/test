# Generated by Django 4.2.2 on 2023-06-08 18:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_alter_place_latitude_alter_place_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
