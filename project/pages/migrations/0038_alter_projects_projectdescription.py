# Generated by Django 3.2.2 on 2023-01-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0037_projects_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='ProjectDescription',
            field=models.TextField(blank=True, null=True),
        ),
    ]
