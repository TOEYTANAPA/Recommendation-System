# Generated by Django 2.0.1 on 2018-03-15 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recommendation', '0011_storebyuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, max_length=10, null=True)),
                ('salary', models.CharField(blank=True, max_length=50, null=True)),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
                ('breakfast', models.BooleanField(default=False)),
                ('lunch', models.BooleanField(default=False)),
                ('dinner', models.BooleanField(default=False)),
                ('late', models.BooleanField(default=False)),
                ('taste', models.BooleanField(default=False)),
                ('price', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
                ('clean', models.BooleanField(default=False)),
                ('at', models.BooleanField(default=False)),
                ('location', models.BooleanField(default=False)),
                ('facebook', models.BooleanField(default=False)),
                ('twitter', models.BooleanField(default=False)),
                ('instagram', models.BooleanField(default=False)),
                ('line', models.BooleanField(default=False)),
                ('japanese', models.BooleanField(default=False)),
                ('thai', models.BooleanField(default=False)),
                ('diet', models.BooleanField(default=False)),
                ('shabu', models.BooleanField(default=False)),
                ('grill', models.BooleanField(default=False)),
                ('steak', models.BooleanField(default=False)),
                ('fastfood', models.BooleanField(default=False)),
                ('cake', models.BooleanField(default=False)),
                ('dessert', models.BooleanField(default=False)),
                ('coffee', models.BooleanField(default=False)),
                ('juice', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
