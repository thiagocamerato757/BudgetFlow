# Use uma imagem oficial do Python como base
FROM python:3.10

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo de dependências para o contêiner
COPY requirements.txt /app

# Instala as dependências
RUN pip install -r requirements.txt

# Copia todo o conteúdo do projeto para o contêiner
COPY . .

# Expõe a porta 8000 para acessar o Django
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["python3", "BudgetFlow/manage.py", "runserver", "0.0.0.0:8000"]
