# Generated by Django 4.1.3 on 2024-04-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='especialidade',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
