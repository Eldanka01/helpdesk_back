# Generated by Django 5.0.4 on 2024-05-08 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auditorium_alter_helpdeskrequest_auditorium_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpdeskrequest',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='helpdeskrequest',
            name='creator',
            field=models.CharField(max_length=100, verbose_name='От'),
        ),
    ]
