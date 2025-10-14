# Projeto Biblioteca

Este é um sistema de gerenciamento de biblioteca desenvolvido em Django para fins educacionais.

## Descrição

O sistema permite gerenciar livros, autores, membros e empréstimos de uma biblioteca. Este projeto foi criado com intuito de demonstrar boas práticas de desenvolvimento e também exemplos de erros comuns que podem ocorrer durante o desenvolvimento.

## Versão Atual

v1.1.0 - Versão com correções dos erros intencionais

## Histórico de Versões

- v1.0.0 - Versão inicial com erros intencionais para demonstração
- v1.1.0 - Versão com correções dos erros identificados

## Estrutura do Projeto

- `biblioteca/` - Configurações do projeto Django
- `books/` - App principal com models de livros, autores, membros e empréstimos
- `ERROS_DOCUMENTACAO.md` - Documentação dos erros intencionais introduzidos
- `CORRECOES_DOCUMENTACAO.md` - Documentação das correções aplicadas

## Erros Intencionais e Correções

A versão inicial (v1.0.0) deste projeto contém erros intencionais documentados no arquivo `ERROS_DOCUMENTACAO.md`. 
Na versão atual (v1.1.0), todos esses erros foram corrigidos e as correções estão documentadas no arquivo `CORRECOES_DOCUMENTACAO.md`.

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual: `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute as migrações: `python manage.py migrate`

## Uso

1. Inicie o servidor: `python manage.py runserver`
2. Acesse http://127.0.0.1:8000/

## Contribuição

Este projeto é para fins educacionais. Contribuições são bem-vindas.

## Licença

MIT