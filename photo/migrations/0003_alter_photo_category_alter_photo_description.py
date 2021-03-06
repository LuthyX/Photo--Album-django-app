# Generated by Django 4.0.3 on 2022-05-27 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_alter_photo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photo.category'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
