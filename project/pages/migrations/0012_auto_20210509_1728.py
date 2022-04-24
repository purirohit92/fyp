# Generated by Django 3.2.2 on 2021-05-09 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='desc',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]
