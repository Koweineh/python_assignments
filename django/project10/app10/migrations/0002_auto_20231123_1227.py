# Generated by Django 2.2.4 on 2023-11-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app10', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='color',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]