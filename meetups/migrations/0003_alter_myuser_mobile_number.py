# Generated by Django 4.0.4 on 2022-07-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_alter_meetup_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
