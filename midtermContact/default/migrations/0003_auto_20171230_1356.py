# Generated by Django 2.0 on 2017-12-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_remove_contact_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='QQnum',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='addr',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
