# Generated by Django 3.0.3 on 2020-08-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studymaterial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studymaterial',
            name='file_title',
            field=models.CharField(default='quick start with pdf', max_length=150),
        ),
        migrations.AddField(
            model_name='studymaterial',
            name='video_title',
            field=models.CharField(default='quick start with video', max_length=150),
        ),
        migrations.AlterField(
            model_name='studymaterial',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='studymaterial',
            name='videos',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
