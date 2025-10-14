# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/spec/v2.0.0.html).

## [1.6.0] - 2025-10-14

### Adicionado
- Sistema de registro de novos usuários
- Painel do usuário com informações de empréstimos e solicitações
- Funcionalidade de devolução de livros pelos próprios usuários
- Verificação de prazos de devolução e destaque de livros atrasados
- Templates para registro de usuários e painel do usuário
- Atualização do README.md com informações sobre as novas funcionalidades

## [1.5.0] - 2025-10-14

### Adicionado
- Sistema de solicitações de empréstimo com aprovação
- Novo model BookRequest para gerenciar solicitações
- Views para solicitar, aprovar e rejeitar empréstimos
- Templates para lista de solicitações e rejeição de solicitações
- Atualização do README.md com informações sobre o novo workflow

## [1.4.4] - 2025-10-14

### Corrigido
- Atualização da documentação com correção de logout
- Versionamento adequado

## [1.4.3] - 2025-10-14

### Corrigido
- Problema com a funcionalidade de logout que redirecionava para uma página em branco
- Remoção de padrões de URL conflitantes para logout
- Implementação de view de logout personalizada

## [1.4.2] - 2025-10-14

### Adicionado
- Atualização da documentação para refletir a versão mais recente

## [1.4.1] - 2025-10-14

### Adicionado
- Template de perfil do usuário faltante
- Configuração completa do Django Admin para todos os models
- Arquivo .gitignore para exclusão de arquivos desnecessários

## [1.4.0] - 2025-10-14

### Adicionado
- Página de perfil do usuário
- Sistema de signals para criação automática de perfis de membro
- Melhorias na experiência do usuário
- Atualização do README.md com informações sobre o perfil de usuário

### Corrigido
- Problemas com logout e navegação
- Tratamento de usuários sem perfis de membro

## [1.3.0] - 2025-10-14

### Adicionado
- Sistema de usuários com diferentes perfis (membro, bibliotecário, administrador)
- Controle de acesso baseado em perfis de usuário
- Funcionalidade de empréstimo de livros para membros
- Funcionalidade de devolução de livros para bibliotecários
- Templates de login e autenticação
- Atualização do README.md com informações sobre os perfis de usuário

## [1.2.0] - 2025-10-14

### Adicionado
- Interface web completa com templates HTML usando Bootstrap
- Página inicial com estatísticas da biblioteca
- Páginas para listar livros, autores, membros e empréstimos
- Comando de gerenciamento para popular o banco de dados com dados de exemplo
- Superusuário padrão para acesso ao admin
- Atualização do README.md com instruções de uso da interface

## [1.1.0] - 2025-10-14

### Corrigido
- Correção de todos os erros intencionais da versão anterior
- Model Author com método __str__ adicionado e ordenação corrigida
- Model Book com related_name adicionado, tipo de campo pages corrigido, referência __str__ corrigida e ordenação corrigida
- Model Member com max_length adicionado ao phone_number e valor padrão corrigido
- Model BorrowRecord com referência __str__ corrigida
- Criação de documentação das correções aplicadas no arquivo CORRECOES_DOCUMENTACAO.md

## [1.0.0] - 2025-10-14

### Adicionado
- Projeto Django inicial para sistema de biblioteca
- Models para Book, Author, Member e BorrowRecord
- Documentação de erros intencionais no arquivo ERROS_DOCUMENTACAO.md
- Arquivo README.md com informações básicas do projeto
- Arquivo CHANGELOG.md para registro de alterações

### Erros Intencionais
- Model Author com ordenação incorreta
- Model Book com ordenação incorreta e referência errada no método __str__
- Model Member com CharField sem max_length e valor padrão incorreto
- Model BorrowRecord com referência incorreta no método __str__
- Ausência do método __str__ no model Author