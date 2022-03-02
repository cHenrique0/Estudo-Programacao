# Tipos de dados

Segundo o [**ECMAScrip standard**](https://tc39.es/ecma262/multipage/) temos _9 tipos de dados_:

## Data Types:
1. **Primitive:**
   - `String`
   - `Number`
   - `Boolean`
   - `undefined`
   - `Symbol`
   - `BigInt`
2. **Structural:**
   - 2.1. _Object_:
     - `Array`
     - `Map`
     - `Set`
     - `Date`
     - `...`
   - 2.2. _Functions_ 
3. **Structural Root Primitve**
   - `null`

## 1. String

- É uma cadeia de caracteres;
- Serve para escrever textos;
- Para definir um string usa-se:
  1. Aspas duplas: `"minha string"`;
  2. Aspas simples: `'minha outra string'`;
  3. Crase: <code>``</code>;
     - a crase serve para template literals ou template strings;
     - serve também para escrever em multiplas linhas;
     - aceita expressões dentro da string(interpolação);
     - além disso, a crase permite escrever `"` e `'` na string;

```js
console.log("Minha primeira string");
console.log('Minha segunda string');
console.log(`Interpolação ${1 + 1}`);
console.log(`Usando 'crase' para "escrever" strings`);
```

## 2. Number

- São os números;
- Dentro do number temos:
    1. Inteiros: `33, 10, 2,...`;
    2. Reais(float): `34.2, 4.5, ...`;
    3. NaN - `Not a Number`; 
    4. Infinito: `Infinity`;


## 3. Boolean

- Tem apenas dois valores:
  - Verdadeiro: `True`;
  - Falso: `False`;


## 4. Null

- Nulo;
- Objeto que não possui nenhum conteúdo;


## 5. Undefined

- Indefinido;
- É algo que não existe;
- Diferente de null;

```js
console.log(null === undefined); // Retorna false 
```

## 6. Object

- Objeto;
- É um tipo de dado estrutural;
- Possui propriedades/atributos e funcionalidades/metodos;
- Definindo um objeto:
  - `{ propriedade: "valor" }`

```js
console.log({
    name: "Marcos",
    age: 23,
    walk: functions() {
        console.log('walking');
    }
})
```

## 7. Arrays

- São vetores;
- É uma lista que agrupa dados;
- Definindo um array:
  - `[dados, dados, dados,...]`

```js
console.log([
    "Milk",
    "Eggs",
    2,
    3
])
```

**[Saiba Mais](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)**