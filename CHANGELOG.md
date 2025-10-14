# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/spec/v2.0.0.html).

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