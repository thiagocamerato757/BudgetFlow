# Generated by Django 5.1.1 on 2024-10-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Gastos", "0002_despesa_categoria_receita_categoria"),
    ]

    operations = [
        migrations.AlterField(
            model_name="despesa",
            name="valor",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="receita",
            name="valor",
            field=models.FloatField(default=0),
        ),
    ]
