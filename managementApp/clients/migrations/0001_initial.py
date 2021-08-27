# Generated by Django 3.2.6 on 2021-08-23 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('phoneNumber', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('priority', models.IntegerField()),
                ('deadline', models.DateField(blank=True)),
                ('responsible_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('priority', models.IntegerField()),
                ('deadline', models.DateField(blank=True)),
                ('responsible_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('subTasks', models.ManyToManyField(blank=True, to='clients.SubTask')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('priority', models.IntegerField()),
                ('deadline', models.DateField(blank=True)),
                ('responsible_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('tasks', models.ManyToManyField(blank=True, to='clients.Task')),
            ],
        ),
    ]
