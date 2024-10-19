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

# Copia o entrypoint.sh para o contêiner e dá permissão de execução
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expõe a porta 8000 para acessar o Django
EXPOSE 8000

# Define o entrypoint do contêiner
ENTRYPOINT ["/app/entrypoint.sh"]
