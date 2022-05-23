# Arrays

Podemos armazenar diversas variáveis do mesmo tipo em uma estrutura de dados do tipo array.  
Para declarar um array precisamos especificar o tipo dos elementos.  
Se quisermos que o array armazene elementos de qualquer tipo, declaramos o array do tipo `object`.  

Sintaxe:
```c#
tipo[] nomeArray;
tipo[] nomeArray = new tipo[] { elementos };
tipo[] nomeArray = new tipo[tamanho];
var nomeArray = new tipo[tamanho];
```
Nas duas primeiras declarações de arrays acima não é necessário informar o tamanho do array. Já na seguintes é obrigatório especificar o tamanho.

Exemplos:
```c#
// Declarando um array unidimensional de inteiros com tamanho 5
int[] array = new int[5];

// Declarando e inicializando um array de inteiros
int[] array2 = new int[] { 1, 3, 5, 7, 9 };

// sintaxe alternativa
int[] array3 = { 1, 2, 3, 4, 5 };

// Declarando um array bidimensional
int[,] array1 = new int[2, 3];

// Declarando e inicializando um array bidimensional
int[,] array2 = { { 1, 2, 3, 4}, { 5, 6, 7, 8 } };
```
## Percorrendo um array
### 1. Usando `for`
```c#
int[] array = { 1, 2, 3, 4, 5};

for (int index = 0; index < array.Length; index++)
{
    Console.WriteLine(array[index]); // mostra os elemendos do array um a um
}
```

### 2. Usando `foreach`
```c#
int[] array = { 1, 2, 3, 4, 5};
            
foreach (var item in array)
{
    Console.WriteLine(item);
}
```
O `var` dentro do `foreach` pode ser trocado pelo tipo do array a ser percorrido.