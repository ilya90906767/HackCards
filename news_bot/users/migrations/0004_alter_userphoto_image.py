# Generated by Django 5.0.7 on 2024-11-30 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_fio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphoto',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]