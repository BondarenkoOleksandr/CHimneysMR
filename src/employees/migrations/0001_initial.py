# Generated by Django 3.2.7 on 2021-09-22 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(null=True, upload_to='employees/')),
                ('position', models.CharField(max_length=100)),
                ('type_of_works', models.TextField()),
                ('state', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.state')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('text', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Normal'), (4, 'Good'), (5, 'Excellent')], default=(5, 'Excellent'))),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]