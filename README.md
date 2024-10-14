# BudgetFlow

**BudgetFlow** é uma aplicação web construída com Django para o gerenciamento de finanças pessoais. Com ela, os usuários podem registrar suas despesas e receitas, além de acompanhar e organizar seus gastos de maneira simples e intuitiva.

## Funcionalidades

- **Autenticação de Usuários**: Acesso controlado por login e senha. Usuários não autenticados são redirecionados para a tela de login.
- **Cadastro de Usuários**: Usuários podem criar uma nova conta e, após o cadastro, são redirecionados para a tela de login.
- **Registro de Receitas e Despesas**: Usuários autenticados podem adicionar suas receitas e despesas.
- **Visualização de Receitas e Despesas**: Permite que os usuários visualizem todas as suas transações em uma lista.
- **Edição e Remoção de Gastos**: Os usuários podem editar ou remover qualquer transação cadastrada.
- **Logout**: Quando o usuário está autenticado, a homepage exibe uma opção para sair da conta atual.

## Fluxo de Navegação

- **Homepage**: A página inicial é o ponto de partida para o usuário.
- **Login**: Ao tentar acessar áreas restritas sem estar autenticado, o usuário será redirecionado para a página de login.
- **Registro de Conta**: Caso o usuário não tenha uma conta, ele pode clicar em "Criar Conta" e preencher seus dados.
- **Gestão de Finanças**: Após a autenticação, o usuário pode adicionar, visualizar, editar ou remover suas transações.
- **Logout**: Após estar autenticado, o usuário pode fazer logout na homepage.

## Tecnologias Utilizadas

- **Django** (Backend)
- **HTML/CSS** (Frontend)
- **SQLite** (Banco de Dados)

## Como Executar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/budgetflow.git
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Execute as migrações:
    ```bash
    python manage.py migrate
    ```
4. Inicie o servidor local:
    ```bash
    python manage.py runserver
    ```
5. Acesse o site em seu navegador:
    ```bash
    http://127.0.0.1:8000
    ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues.

[Ver Projeto no GitHub](https://github.com/seu-usuario/budgetflow)
