Título: Desenvolvimento de CRUD para Cadastro de usuários utilizando Node.js e Flask

Objetivo:
Desenvolver um sistema de gerenciamento de usuários com as operações básicas de CRUD (Create, Read, Update, Delete) utilizando Node.js para o backend e Flask para o frontend.

Tecnologias Utilizadas:

Node.js: Ambiente de execução JavaScript no servidor.
Express.js: Framework web para Node.js utilizado para criar o servidor HTTP.
MySQL: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar os dados dos usuários.
MongoDB: Sistema de gerenciamento de banco de dados não relacional utilizado para armazenar os dados dos usuários.
Flask: Microframework web em Python utilizado para renderizar as páginas HTML e interagir com o banco de dados.


Funcionalidades Implementadas:

Cadastro de usuários (Create):
Formulário para adicionar novas usuários.
Rota para receber os dados do formulário e inserir um novo usuários no banco de dados.
Listagem de usuários (Read):
Tabela para exibir todas os usuários cadastradas.
Consulta ao banco de dados para recuperar todas os usuários cadastradas.
Edição de usuários (Update):
Botão de edição em cada linha da tabela de usuários.
Página de edição com formulário preenchido com os dados do usuário selecionada.
Rota para receber os dados do formulário e atualizar o usuário correspondente no banco de dados.
Exclusão de usuários (Delete):
Botão de exclusão em cada linha da tabela de usuários.
Rota para receber o ID do usuário a ser excluída e removê-la do banco de dados.


Estrutura do Projeto:

Node.js Backend:
Arquivo server.js: Configuração do servidor Express.js e definição das rotas CRUD.
Pasta controllers: Contém os arquivos de controle de toda a aplicação.
Pasta routes: Contém os arquivos das rotas para cada operação CRUD.
Pasta templates: Contém os arquivos HTML para renderização das páginas.
Flask Frontend:
Arquivo index.py: Configuração do servidor Flask e definição das rotas para renderização das páginas.
Pasta templates: Contém os arquivos HTML das páginas renderizadas pelo Flask.


Instruções de Uso:

Clonar o repositório do projeto.
Instalar as dependências Node.js utilizando o comando npm install.
Configurar o banco de dados MySQL.
Executar o servidor Node.js utilizando o comando npm run dev.
Acessar a aplicação web no navegador utilizando o endereço fornecido pelo servidor.
