# Generated by Django 2.0.2 on 2018-03-04 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='populations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chromosome1', models.CharField(max_length=1)),
                ('chromosome2', models.CharField(max_length=1)),
                ('chromosome3', models.CharField(max_length=1)),
                ('chromosome4', models.CharField(max_length=1)),
                ('chromosome5', models.CharField(max_length=1)),
                ('chromosome6', models.CharField(max_length=1)),
                ('chromosome7', models.CharField(max_length=1)),
                ('chromosome8', models.CharField(max_length=1)),
                ('chromosome9', models.CharField(max_length=1)),
                ('chromosome10', models.CharField(max_length=1)),
            ],
        ),
    ]
