# Generated by Django 3.0.3 on 2020-03-09 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0018_auto_20200309_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journaltable',
            name='to_be_listed',
        ),
    ]
