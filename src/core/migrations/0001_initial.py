# Generated by Django 3.2.7 on 2021-09-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='locations/first_screen/')),
            ],
            options={
                'verbose_name_plural': 'First Screen',
            },
        ),
        migrations.CreateModel(
            name='SecondScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=250)),
                ('main_description', models.TextField()),
                ('sec_title', models.CharField(max_length=250)),
                ('sec_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Second Screen',
            },
        ),
        migrations.CreateModel(
            name='ThirdScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=250)),
                ('main_description', models.TextField()),
                ('sec_title', models.CharField(max_length=250)),
                ('sec_description', models.TextField()),
                ('thrd_title', models.CharField(max_length=250)),
                ('thrd_description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='cities/third_screen/')),
            ],
            options={
                'verbose_name_plural': 'Third Screen',
            },
        ),
    ]