# Generated by Django 3.2.4 on 2021-07-06 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='cast_image',
            field=models.ImageField(default='default.jpg', upload_to='cast'),
        ),
        migrations.AddField(
            model_name='review',
            name='poster',
            field=models.ImageField(default='default.jpg', upload_to='poster'),
        ),
    ]
