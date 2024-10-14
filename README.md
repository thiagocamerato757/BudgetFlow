# BudgetFlow

**BudgetFlow** é uma aplicação web desenvolvida para o gerenciamento de finanças pessoais, permitindo aos usuários registrar receitas e despesas, além de visualizar e editar suas transações. Este projeto foi construído utilizando Django como framework principal.

## Escopo do Site

O site BudgetFlow oferece funcionalidades básicas para controle de finanças pessoais, incluindo:
- **Autenticação de Usuários**: Criação de contas, login e logout.
- **Gerenciamento de Transações**: Adicionar, visualizar, editar e remover receitas e despesas.
- **Navegação Segura**: Usuários não autenticados são redirecionados para a página de login ao tentar acessar áreas restritas.
- **Logout**: Uma opção de logout é exibida na homepage quando o usuário está autenticado.

## Manual do Usuário

### Cadastro de Usuário

1. Na página inicial, clique em **Criar Conta**.
2. Preencha o formulário de registro com seu nome de usuário, e-mail e senha.
3. Após o envio do formulário, você será redirecionado para a página de login.
4. Faça login com as credenciais recém-criadas.

### Login e Logout

- **Login**: Após o registro, ou se já tiver uma conta, clique em **Entrar** na página inicial, insira suas credenciais e faça login.
- **Logout**: Quando estiver autenticado, na página inicial será exibida a opção **Sair**. Clique nela para sair da sua conta.

### Adicionar Receitas/Despesas

1. Após o login, acesse a página **Adicionar Receita** ou **Adicionar Despesa**.
2. Preencha o formulário com os detalhes da transação (valor, descrição, data).
3. Submeta o formulário para salvar a transação no sistema.

### Visualizar, Editar e Remover Transações

1. Após o login, clique em **Ver Receitas/Despesas** para visualizar todas as suas transações.
2. Você pode clicar no botão **Editar** para modificar qualquer transação existente.
3. Para remover uma transação, clique no botão **Remover** ao lado da transação correspondente.

### Fluxo de Redirecionamento

- Se o usuário tentar acessar funcionalidades como adicionar ou visualizar transações sem estar autenticado, será automaticamente redirecionado para a página de login.

## Funcionalidades Implementadas

- **Autenticação de Usuários**: Login, logout e criação de contas funcionam corretamente.
- **Adição de Receitas e Despesas**: O processo de adição de transações foi testado e está funcionando.
- **Visualização de Transações**: Todas as transações cadastradas são listadas corretamente.
- **Edição de Transações**: O recurso de edição foi testado e está funcionando.
- **Remoção de Transações**: O recurso de remoção foi testado e está funcionando.
- **Redirecionamento de Usuários**: Usuários não autenticados são corretamente redirecionados para a tela de login ao tentar acessar funcionalidades restritas.

## O que não Funcionou

- **Nenhuma falha foi identificada até o momento**.

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

## Componentes do Grupo

- **Thiago Pereira Camerato**
- **Marcos Turo Fernandes Junior**


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues.

[Ver Projeto no GitHub](https://github.com/seu-usuario/budgetflow)
