## Tipos de Referência e Tipos de Valor

- A memória é dividida em duas partes:
    - **Heap**: Armazena os dados;
    - **Stack**: Armazena as referências(endereços) para os dados;
- Qualquer tipo no `.Net` é tratado como:
    - Tipo de referência(_Reference Type_);
    - Tipo de valor(_Value Type_);

## 1. Value Types

- **Value Types** armazeman dados em um local da memória chamada **Stack**;
- Quando armazenamos um valor, a memória é alocada;
- Este espaço armazena o dado criado;
- A variável acessa este dado diretamente;
- Se assimilarmos uma variável do **value type** a outra, o valor será **COPIADO**, e ambas serãi independentes;
- `Built-in`, `Structs` e `Enums` são sempre **Value Types**;
- o _Garbage Collector_ não acessa o **Stack**;

```c#
int x = 25;
int y = x;  // Y é uma cópia de x
Console.WriteLine(x);   // imprime 25
Console.WriteLine(y);   // imprime 25
x = 32;
Console.WriteLine(x);   // imprime 32
Console.WriteLine(y);   // imprime 25, pois somente o x foi alterado
```

## 2. Reference Types

- Armazenam o endereço do objeto que contém os dados;
- Não armazena os dados em si;
- Saõ armazenados em um local da memória chamado de **Heap**;
- Ao assimilar um variável:
    - Criará uma _referência_;
    - Aponta para a mesma informação;
    - Não são independentes;
- Quando não mais utilizados, são marcados para exclusão;
    - O **Garbage Collector** passa removento todos eles;
- `Class`, `Objects`, `Arrays`, entre outros, são **Reference Types**;

```c#
var arr = new string[2];
arr[0] = "Item 1";
var arr2 = arr; // Não cria uma copia

Console.WriteLine(arr[0]);  // imprime "Item 1"
Console.WriteLine(arr2[0]); // imprime "Item 1"

arr[0] = "Item alterado";
Console.WriteLine(arr[0]);  // imprime "Item alterado"
Console.WriteLine(arr2[0]); // imprime "Item alterado"
```