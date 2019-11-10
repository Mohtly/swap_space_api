# Generated by Django 2.2.5 on 2019-11-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.TextField()),
                ('value_low', models.IntegerField()),
                ('value_high', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('description', models.TextField()),
                ('traded', models.BooleanField()),
                ('date_time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]