# Projeto Biblioteca

Este é um sistema de gerenciamento de biblioteca desenvolvido em Django para fins educacionais.

## Descrição

O sistema permite gerenciar livros, autores, membros e empréstimos de uma biblioteca. Este projeto foi criado com intuito de demonstrar boas práticas de desenvolvimento e também exemplos de erros comuns que podem ocorrer durante o desenvolvimento.

## Versão Atual

v1.4.3 - Versão com correção da funcionalidade de logout

## Histórico de Versões

- v1.0.0 - Versão inicial com erros intencionais para demonstração
- v1.1.0 - Versão com correções dos erros identificados
- v1.2.0 - Versão com interface web completa e dados de exemplo
- v1.3.0 - Versão com sistema de usuários e controle de acesso
- v1.4.0 - Versão com perfil de usuário e melhorias na experiência do usuário
- v1.4.1 - Versão com template de perfil e configuração do admin
- v1.4.2 - Versão com documentação atualizada
- v1.4.3 - Versão com correção da funcionalidade de logout

## Estrutura do Projeto

- `biblioteca/` - Configurações do projeto Django
- `books/` - App principal com models de livros, autores, membros e empréstimos
- `templates/` - Templates HTML para a interface web
- `ERROS_DOCUMENTACAO.md` - Documentação dos erros intencionais introduzidos
- `CORRECOES_DOCUMENTACAO.md` - Documentação das correções aplicadas

## Interface Gráfica

O sistema agora possui uma interface web completa com as seguintes páginas:
- Página inicial com estatísticas da biblioteca
- Lista de livros
- Lista de autores
- Lista de membros (apenas para bibliotecários e administradores)
- Lista de empréstimos (apenas para bibliotecários e administradores)
- Perfil do usuário

## Sistema de Usuários e Controle de Acesso

O sistema implementa diferentes níveis de acesso baseados em perfis de usuário:

### Perfis de Usuário

1. **Membros Comuns**:
   - Podem visualizar livros e autores
   - Podem solicitar empréstimos de livros disponíveis
   - Podem visualizar seu próprio histórico de empréstimos
   - Podem visualizar e editar seu perfil

2. **Bibliotecários**:
   - Possuem todos os privilégios dos membros comuns
   - Podem gerenciar membros
   - Podem controlar empréstimos e devoluções
   - Podem acessar relatórios detalhados

3. **Administradores**:
   - Possuem todos os privilégios dos bibliotecários
   - Podem acessar o painel administrativo do Django

### Usuários de Exemplo

Ao executar o comando `populate_db`, os seguintes usuários são criados:

- **joao_silva** - Senha: password123 (Membro)
- **maria_santos** - Senha: password123 (Membro)
- **pedro_costa** - Senha: password123 (Membro)
- **ana_bibliotecaria** - Senha: password123 (Bibliotecária)
- **carlos_admin** - Senha: password123 (Administrador)

## Funcionalidades

- **Login/Logout**: Sistema de autenticação completo
- **Perfil de Usuário**: Visualização e gerenciamento de informações pessoais
- **Empréstimos**: Membros podem solicitar empréstimos de livros disponíveis
- **Devoluções**: Bibliotecários podem registrar devoluções de livros
- **Controle de Acesso**: Diferentes funcionalidades baseadas no perfil do usuário
- **Administração**: Interface administrativa completa para gerenciamento de dados

## Erros Intencionais e Correções

A versão inicial (v1.0.0) deste projeto contém erros intencionais documentados no arquivo `ERROS_DOCUMENTACAO.md`. 
Na versão atual (v1.1.0), todos esses erros foram corrigidos e as correções estão documentadas no arquivo `CORRECOES_DOCUMENTACAO.md`.

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual: `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute as migrações: `python manage.py migrate`

## Popular o Banco de Dados

Para popular o banco de dados com dados de exemplo:
```
python manage.py populate_db
```

## Criar Superusuário

Para criar um superusuário para acessar o admin:
```
python manage.py createsuperuser
```

## Uso

1. Inicie o servidor: `python manage.py runserver`
2. Acesse http://127.0.0.1:8000/ para a interface web
3. Faça login com um dos usuários de exemplo listados acima
4. Acesse http://127.0.0.1:8000/admin/ para o painel administrativo (usuário: admin, senha: admin123)

## Contribuição

Este projeto é para fins educacionais. Contribuições são bem-vindas.

## Licença

MIT