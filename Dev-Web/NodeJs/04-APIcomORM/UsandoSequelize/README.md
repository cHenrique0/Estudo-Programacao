# Criação de uma API usando o Sequelize

## Sequelize
É um ORM

## Ferramentas
- Node.js
- TypeScript
- Express
- PostgreSQL
- Sequelize

## Operações da API:

| Metódo   | Url                            | Ação                                                |
| :------- | :----------------------------- | :-------------------------------------------------- |
| `GET`    | api/tutorials                  | obter todos os tutorias                             |
| `GET`    | api/tutorials/:id              | obter tutorial por id                               |
| `POST`   | api/tutorials                  | adicionar um tutorial                               |
| `PUT`    | api/tutorials/:id              | atualizar um tutorial por id                        |
| `DELETE` | api/tutorials/:id              | deleter um tutorial por id                          |
| `DELETE` | api/tutorials                  | deletar todos os tutoriais                          |
| `GET`    | api/tutorials/published        | encontrar todos os tutoriais publicados             |
| `GET`    | api/tutorials?title=[key_word] | encontrar um tutorial cujo titulo contém 'key_word' |

