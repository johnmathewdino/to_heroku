# Generated by Django 3.2.7 on 2022-01-05 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_loggedinuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoggedInUser',
        ),
    ]