# Generated by Django 3.2.2 on 2023-01-24 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0038_alter_projects_projectdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone', models.CharField(blank=True, max_length=12, null=True)),
                ('Amount', models.FloatField(blank=True, null=True)),
                ('Description', models.TextField(blank=True)),
            ],
        ),
    ]
