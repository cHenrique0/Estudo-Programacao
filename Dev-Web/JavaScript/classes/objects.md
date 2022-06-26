# Objetos

Um _objeto_ é um valor composto. Ele agrega disversos valores que podem ser primitivos ou outros objetos.  
Um objeto é um conjunto não ordenado de _propriedades_, cada uma tendo um nome e um valor.  
Além de possuir seu próprio conjunto de propriedades, um objeto JavaScript também herda as propriedades de outro objeto, conhecido como seu **protótipo**. Normalmente, os métodos de um objeti são propriedades herdadas e essa _herança de protótipos_ é um recurso importante do JavaScript.  
  
Os objetos são _dinâmicos_: suas propriedades podem ser adicionadas e excluídas.  
**Qualquer** valor em JavaScript que não seja `string`, `number`, `true`, `false`, `null` ou `undefined`, é um objeto.  
Os objetos são _mutáveis_ e são manipulados por **referência** e não por valor.  
  
Uma _propriedade_ tem um nome e um valor. Um nome de propriedade pode ser qualquer string, incluindo a string vazia, mas nenhum objeto pode ter duas propriedades com o mesmo nome. O valor pode ser qualquer valor de JavaScript ou uma função _"getter"_ ou _"setter"_(ou ambas).  
  
Além de nome e valor, cada propriedade tem valores associados que são chamados de _atributos de propriedade_:

- O atributo _gravável_ indica se o valor da propriedade pode ser configurado.
- O atributo _enumerável_ indica se o nome da prorpriedade é retornado por um laço `for/in`.
- O atributo _configurável_ indifca se a propriedade pode ser excluída e seus atributos podem ser alterados.
  
Além de propriedades, todo objeto tem 3 _atributos de objeto_ associados:
- O _protótipo_ de um objeto é uma referência para outro objeto do qual as propriedades são herdadas.
- A _classe_ de um objeto é uma string que classifica o tipo de um objeto.
- A flag _extensível_ de um objeto indica se novas propriedades podem ser adicionadas.

## 1. Criando um objeto
Objetos podem ser criado com objetos literais, com a palavra-chave `new` e com a função `Object.create()`.

### 1.1 Objetos literais
Um _objeto literal_ é uma lista separada com vírgulas de pares _nome: valor_ colocados entre chaves.  
Um nome de propriedade é um identificador JavaScript ou uma string literal.  
Um valor de propriedade é qualquer expressão JavaScript. O valor da expressão, que pode ser um valor primitivo ou um valor de objeto, se troca o valor da propriedade.
```js
// Um objeto vazio(sem propriedades)
let empty = {};

// Um objeto com duas propriedades
let point = {
    x: 0,
    y: 0
};

// um objeto em que as propriedades possuem valores com expressões
let point2 = {
    x: point.x,
    y: point.y+1
};

/*
Um objeto onde os nomes das propriedades possuem espaçoes e hifens, por isso usam string literals.
for é uma palavra reservada, por isso usa aspas.
*/
let book = {
    "main title": "JavaScript",
    'sub-title': "The definitive guide",
    "for": "all audiences",

    // O valor da propriedade é outro objeto. Note que os nomes das propriedades não tem aspas.
    author: {
        firstname: "David",
        surname: "Flanagan"
    }
}
```

### 1.2 `new`
O operador `new` cria e inicializa um novo objeto.  
JavaScript contém construtores internos para tipos nativos:
```js
let o = new Object();       // cria um objeto vazio: equivale a {}
let a = new Array();        // cria um array vazio: equivale a []
let d = new Date();         // cria um objeto Date com a hora atual
let r = new RegExp("js");   // cria um objeto RegExp para comparação de padrões
```
Além de construtores internos, podemos definir nossas próprias funções construtoras.

### 1.3 `Object.create()`


## 2. Consultando e configurando propriedades

