# Generated by Django 3.2.2 on 2021-05-16 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_listingimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ListingImage',
        ),
        migrations.AlterField(
            model_name='mybooking',
            name='room_select',
            field=models.CharField(choices=[('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106')], default='0', max_length=255, null=True),
        ),
    ]
