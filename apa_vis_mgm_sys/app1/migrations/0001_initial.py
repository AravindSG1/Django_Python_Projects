# Generated by Django 5.1.6 on 2025-04-10 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100, verbose_name='category')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('phone_number', models.CharField(max_length=20, verbose_name='phone_number')),
                ('address', models.CharField(max_length=400, verbose_name='address')),
                ('apartment_number', models.IntegerField(verbose_name='apartment_number')),
                ('floor', models.CharField(max_length=10, verbose_name='floor')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('pass_desc', models.CharField(max_length=100, verbose_name='pass_desc')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100, verbose_name='category')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20, verbose_name='phone_number')),
                ('address', models.CharField(max_length=400, verbose_name='address')),
                ('apartment_number', models.IntegerField(verbose_name='apartment_number')),
                ('floor', models.CharField(max_length=10, verbose_name='floor')),
                ('to_meet', models.CharField(max_length=100, verbose_name='to_meet')),
                ('reason', models.CharField(max_length=100, verbose_name='reason')),
            ],
        ),
    ]
