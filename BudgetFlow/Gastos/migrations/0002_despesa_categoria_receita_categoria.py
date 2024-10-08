# Generated by Django 5.1.1 on 2024-10-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gastos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='categoria',
            field=models.CharField(choices=[('alimentacao', 'Alimentação'), ('transporte', 'Transporte'), ('educacao', 'Educação'), ('moradia', 'Moradia'), ('saude', 'Saúde'), ('lazer', 'Lazer'), ('roupas', 'Roupas'), ('servicos', 'Serviços'), ('outros', 'Outros')], default='Outros', max_length=20),
        ),
        migrations.AddField(
            model_name='receita',
            name='categoria',
            field=models.CharField(choices=[('salario', 'Salário'), ('freelancer', 'Freelancer'), ('investimentos', 'Investimentos'), ('presentes', 'Presentes'), ('aluguel', 'Aluguel'), ('venda_bens', 'Venda de Bens'), ('outros', 'Outros')], default='Outros', max_length=20),
        ),
    ]
