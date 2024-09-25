# Generated by Django 5.1.1 on 2024-09-15 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(help_text='Digite o nome de usuário', max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(help_text='Digite a senha', max_length=100)),
                ('total_depesas', models.FloatField(default=0)),
                ('total_receita', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor', models.FloatField(default=0)),
                ('decricao', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.user')),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor', models.FloatField(default=0)),
                ('decricao', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.user')),
            ],
        ),
    ]