# Generated by Django 4.0.2 on 2022-11-09 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plitterprofile',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to='apps.PlitterProfile'),
        ),
    ]