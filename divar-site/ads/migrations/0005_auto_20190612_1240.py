# Generated by Django 2.2.1 on 2019-06-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_auto_20190612_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='city',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='state',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
