# Generated by Django 4.0.5 on 2022-06-06 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address_street', models.CharField(max_length=100)),
                ('address_number', models.CharField(max_length=100)),
                ('address_city', models.CharField(max_length=100)),
                ('address_state', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
