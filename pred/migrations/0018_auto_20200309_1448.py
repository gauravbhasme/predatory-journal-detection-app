# Generated by Django 3.0.3 on 2020-03-09 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0017_auto_20200309_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journaltable',
            name='Number_of_Editors',
            field=models.CharField(choices=[('2', 'More than 7'), ('1', 'Between 5-7'), ('0', 'Lower than 5')], max_length=200),
        ),
    ]
