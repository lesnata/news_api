# Generated by Django 3.1.6 on 2021-02-07 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_published']},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date_published']},
        ),
    ]
