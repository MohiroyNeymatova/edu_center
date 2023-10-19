# Generated by Django 4.1.6 on 2023-10-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'mentor'), (2, 'reception'), (3, 'accountant'), (4, 'director')], null=True),
        ),
    ]