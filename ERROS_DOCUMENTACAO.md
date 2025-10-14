# Documentação de Erros do Sistema de Biblioteca

Este documento registra os erros intencionais introduzidos no sistema de biblioteca Django para fins de demonstração.

## Erros identificados ao executar `makemigrations`

```
SystemCheckError: System check identified some issues:
ERRORS:
books.Author: (models.E015) 'ordering' refers to the nonexistent field, related field, or lookup 'lastname'.
books.Book: (models.E015) 'ordering' refers to the nonexistent field, related field, or lookup 'book_title'.
books.Member.phone_number: (fields.E120) CharFields must define a 'max_length' attribute.
```

## Erros nos Models

### Model Author
1. **Missing `__str__` method**: O método `__str__` não foi implementado, o que causará problemas na exibição dos autores no admin do Django.
2. **Ordenação incorreta**: No Meta class, o campo de ordenação está como `lastname` mas deveria ser `last_name`.

### Model Book
1. **Related name ausente**: No campo `author`, falta o parâmetro `related_name`.
2. **Tipo de campo incorreto**: O campo `pages` está definido como `CharField` quando deveria ser `IntegerField`.
3. **Referência incorreta no `__str__`**: Na função `__str__`, está sendo usado `self.authors.name` em vez de `self.author`.
4. **Ordenação incorreta**: No Meta class, o campo de ordenação está como `book_title` mas deveria ser `title`.

### Model Member
1. **Falta de max_length**: No campo `phone_number`, o `CharField` não tem o parâmetro `max_length` definido.
2. **Tipo de valor padrão incorreto**: O campo `is_active` tem `default="True"` (string) quando deveria ser `default=True` (booleano).

### Model BorrowRecord
1. **Referência incorreta no `__str__`**: Na função `__str__`, está sendo usado `self.member.users.username` em vez de `self.member.user.username`.

## Como identificar esses erros

Esses erros podem ser identificados ao:
- Executar migrações (`python manage.py makemigrations`)
- Acessar o admin do Django
- Tentar criar ou visualizar objetos através das views
- Executar testes automatizados

## Correções necessárias

Para corrigir esses erros, seria necessário ajustar os models conforme as boas práticas do Django.