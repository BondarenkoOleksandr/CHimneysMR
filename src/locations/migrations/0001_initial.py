# Generated by Django 3.2.7 on 2021-09-22 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('description', models.TextField(null=True)),
                ('zip', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TSState',
            fields=[
                ('thirdscreen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.thirdscreen')),
                ('state', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.state')),
            ],
            bases=('core.thirdscreen',),
        ),
        migrations.CreateModel(
            name='TSCity',
            fields=[
                ('thirdscreen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.thirdscreen')),
                ('city', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.city')),
            ],
            bases=('core.thirdscreen',),
        ),
        migrations.CreateModel(
            name='SSState',
            fields=[
                ('secondscreen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.secondscreen')),
                ('state', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.state')),
            ],
            bases=('core.secondscreen',),
        ),
        migrations.CreateModel(
            name='SSCity',
            fields=[
                ('secondscreen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.secondscreen')),
                ('city', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.city')),
            ],
            bases=('core.secondscreen',),
        ),
        migrations.CreateModel(
            name='FSState',
            fields=[
                ('firstscreen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.firstscreen')),
                ('state', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.state')),
            ],
            bases=('core.firstscreen',),
        ),
        migrations.CreateModel(
            name='FSCity',
            fields=[
                ('firstscreen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.firstscreen')),
                ('city', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.city')),
            ],
            bases=('core.firstscreen',),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.state'),
        ),
    ]