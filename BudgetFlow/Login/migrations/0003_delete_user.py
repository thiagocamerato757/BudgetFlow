# Generated by Django 5.1.1 on 2024-09-29 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_remove_receita_user_remove_user_username_user_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]