# Generated by Django 2.2.4 on 2019-09-02 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0008_auto_20190901_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
