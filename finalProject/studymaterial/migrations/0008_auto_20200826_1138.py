# Generated by Django 3.1 on 2020-08-26 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studymaterial', '0007_assignmentpdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(blank=True, to='studymaterial.Choice'),
        ),
    ]
