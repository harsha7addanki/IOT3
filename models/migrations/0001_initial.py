# Generated by Django 3.2.4 on 2021-06-27 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('dev_secret', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('type', models.CharField(choices=[('I', 'Integer'), ('S', 'String'), ('B', 'Boolean'), ('D', 'Decimal')], max_length=64)),
                ('key', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.device')),
                ('properties', models.ManyToManyField(blank=True, to='models.Property')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=64)),
                ('devices', models.ManyToManyField(blank=True, to='models.Device')),
                ('things', models.ManyToManyField(blank=True, to='models.Thing')),
            ],
        ),
    ]
