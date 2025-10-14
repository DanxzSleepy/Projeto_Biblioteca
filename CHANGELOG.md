# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/spec/v2.0.0.html).

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