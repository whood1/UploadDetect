# Generated by Django 2.2.4 on 2019-09-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_auto_20190901_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='d',
        ),
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='title',
            field=models.CharField(max_length=3),
        ),
    ]