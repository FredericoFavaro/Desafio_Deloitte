# Agência Cronos Dashboard (Desafio_Deloitte)

Trata-se de um sistema simples **para gerenciar os integrantes da Equipe Cronos, bem como os Serviços prestados pela empresa e as postagens do blog**.
O sistema foi desenvolvido **back-end** em **Python/Django** com o auxilio do **Bootstrap 5** para o front-end. Para o banco de dados usado foi o SQLite3. A escolha dessas tecnologias se deu devido a agilidade para entregar um produto funcional e robusto.

## Dependências

- Python 3.10
- asgiref 3.5.0
- Django 4.0.2
- sqlparse 0.4.2
- SQL 3.35.5

## Instalação

- Baixar o repositório no seu computador:
`git clone https://github.com/FredericoFavaro/Dsafio_Deloitte.git`

- Instalar as dependências do python:
`pip install -r requirements.txt`

## Features

- [x] CRUD completo para gerenciamento dos dados (Postagens, Serviços, Equipe)
- [x] Banco de dados de teste no repositório
- [x] Responsivo
- [x] Pode ser facilmente adaptado para outros projetos similares

## Features a serem implementadas

- [] Configurar a data de postagem para que seja gerada e modificada automaticamente quando for publicado ou editado respectivamente.
- [] Incluir campo de busca em cada CRUD
- [] Melhorar segurança do sistema incluindo credenciamento 
- [] Criar uma landing page apresentando a empresa, serviços e funcionários interligando as informações dos bancos de dados, ou seja, as informações da langing page serão atualizadas automaticamente sempre que tiver alteração no banco.
- [] Criar um link na landing page para as postagens no blog da empresa.
- [] Permitir incluir imagens nas postagens e no cadastro dos funcionários.
- [] Refatorar o código para melhorar a legibilidade e futuras manutenções.
- [] Criar CSS para padronizar as janelas e facilitar futuras manutenções.
- [] Adicionar confirmação para deletar os dados.
- [] Criar apps django separados para cada CRUD, bem como para o dashboard.
- [] Melhorar a responsividade
- [] Melhorar a estética e UX do sistema.
  ...