# Generated by Django 4.1.5 on 2023-01-14 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ghkj', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
