# Generated by Django 3.0.3 on 2020-03-08 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0012_auto_20200308_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journaltable',
            name='Email_of_Editor',
            field=models.CharField(choices=[('2', 'official'), ('1', 'gmail'), ('0', 'not available')], max_length=200),
        ),
    ]
