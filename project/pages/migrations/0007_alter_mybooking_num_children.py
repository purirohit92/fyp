# Generated by Django 3.2.2 on 2021-05-09 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_mybooking_num_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybooking',
            name='num_children',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
