#!/bin/sh

# Aplica migrações no banco de dados
echo "Applying database migrations..."
python3 BudgetFlow/manage.py migrate --no-input

# Cria um superusuário automaticamente (opcional)
# echo "Creating superuser..."
# python3 BudgetFlow/manage.py createsuperuser --no-input --username admin --email admin@example.com

# Inicia o servidor Django
echo "Starting Django server..."
exec python3 BudgetFlow/manage.py runserver 0.0.0.0:8000
