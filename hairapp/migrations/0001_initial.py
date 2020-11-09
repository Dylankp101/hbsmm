# Generated by Django 3.1.1 on 2020-11-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.TextField(max_length=45)),
                ('phone', models.IntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255)),
            ],
        ),
    ]