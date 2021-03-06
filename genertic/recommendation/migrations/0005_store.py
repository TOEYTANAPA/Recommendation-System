# Generated by Django 2.0.2 on 2018-03-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_auto_20180305_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('place', models.CharField(max_length=200)),
                ('tags', models.CharField(blank=True, max_length=500, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
