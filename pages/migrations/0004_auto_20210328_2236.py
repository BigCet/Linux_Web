# Generated by Django 3.1.7 on 2021-03-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_contact_instagram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
