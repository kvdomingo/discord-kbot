# Generated by Django 3.1.4 on 2020-12-24 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20201225_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='english_name',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
