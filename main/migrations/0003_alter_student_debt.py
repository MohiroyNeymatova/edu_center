# Generated by Django 4.1.6 on 2023-10-17 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=22),
        ),
    ]