# Generated by Django 3.1.1 on 2021-03-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_notice_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
