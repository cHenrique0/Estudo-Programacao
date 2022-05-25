# Listas

Lista é uma estrutura de dados:
- Homogênea: seus elementos são do mesmo tipo
- Ordenada: os elementos são acessados por meio de posições
- Tamanho variável: seus elementos podem ser alocados sob demanada
- Cada elemento ocupa um "nó" da lista
- Classe: `List`
- Namespace: `System.Collections.Generic`

```c#
// declaração de uma lista
List<tipo> lista1;
// instanciação da lista depois da declaração
lista1 = new List<tipo>();

// declaração e instanciação de uma lista
List<tipo> lista2 = new List<tipo>();

// declaração, instanciação e inicialização de uma lista
List<tipo> lista3 = new List<tipo>() { elementos };
```

## 1. `Count`
Retorna o tamanho da lista
```c#
List<string> list = new List<string>() {"Maria", "Bob", "Ana"};
list.Count // retorna 3
```

## 2. `Count(expression)`
Retorna a quantidade de itens que satisfazem a `expression` passada como argumento.  
```c#
List<int> list = new List<int>() { 0, 2, 5, 5, 3, 8, 5};
list.Count(x => x == 5); // retorno: 3
```

## 3. `Add(item)`
Adiciona um elemento ao final da lista
```c#
List<string> list = new List<string>();
list.Add("Maria");
list.Add("Alex");
list.Add("Bob");
list.Add("Ana");
// list = { "Maria", "Alex", "Bob", "Ana" }
```

## 4. `AddRange(items)`
Adiciona vários itens na lista.  
O argumento `items` deve ser um `Enumerable`.
```c#
List<string> list = new List<string>() { "Maria", "Alex" };
List<string> addList = new List<string>() { "Bob", "Ana", "Marcos" };
// list = { "Maria", "Alex" }
list.AddRange(addList);
// list = { "Maria", "Alex", "Bob", "Ana", "Marcos" }
```

## 5. `Insert(index, item)`
Adiciona um elemento na posição(index) passada como argumento
```c#
List<string> list = new List<string>() {"Maria", "Bob", "Ana"};
// list = {"Maria", "Bob", "Ana"}
list.Insert(2, "Alex"); // insere o elemento no indice 2
// list = { "Maria", "Bob", "Alex", "Ana" }
```

## 6. `Where(expression)`
Faz consultas usando `expressions` como argumentos.  
O retorno da consulta é um `IEnumerable`(um tipo de lista).
O método `Where` fica no namespace `using System.Linq`.  
```c#
List<string> list = new List<string>() { 0, 2, 5, 5, 3, 8, 5};
var query = list.Where(x => x == 5);
// query = { 5, 5, 5 }

foreach (var item in query)
{
    Console.WriteLine(item);
}
```

## 7. `First(expression)`
Retorna o **primeiro** elemento que satisfaz a `expression` passada como argumento.  
```c#
List<int> list = new List<int>() { 0, 2, 5, 5, 3, 8, 5};
var query = list.First(x => x == 5);
// query é o 5 do indice 2
```

## 8. `Any(expression)`
Verifica a existencia do item que satisfaz a `expression` passada como argumento.  
Retorna `True` se a lista contém o item ou `False` caso constrário.  
```c#
List<string> list = new List<string>() { "Maria", "Alex", "Bob", "Ana", "Marcos" };
list.Any(x => x == "Bob");   // retorno: True
list.Any(x => x == "Paulo"); // retorno: False
```

## 9. `Skip(count)` & `Take(count)`
`Skip()` pula/ignora uma certa quantidade (`count`) de itens de acordo com o informado como argumento.  
`Take()` "pega" os itens de acordo com a quantidade informada como argumento.  
Ambos os métodos retornam um `IEnumerable`.  
```c#
List<string> list = new List<string>() { "Maria", "Alex", "Bob", "Ana", "Marcos" };

var skip = list.Skip(1); // skip = { "Alex", "Bob", "Ana", "Marcos" }
var take = list.Take(3); // take = { "Maria", "Alex", "Bob" }

// "Maria" e "Alex" são ignorados
foreach (var item in list.Skip(2))
{
    Console.WriteLine(item);
}

// Pega os 3 primeiros: "Maria", "Alex", "Bob"
foreach (var item in list.Take(3))
{
    Console.WriteLine(item);
}

// Combinando os dois métodos: "Bob", "Ana"
foreach (var item in list.Skip(2).Take(2))
{
    Console.WriteLine(item);
}
```

## 10. `Find(expression)` & `FindLast(expression)`
`Find()` retorna a primeira ocorrência de um item na lista que satisfaz a `expression` passada como argumento. `FindLast()` retorna a ultima ocorrência.
```c#
List<string> list = new List<string>() { "Maria", "Alex", "Bob", "Ana", "Marcos" };
var first = list.Find(x => x[0] == 'M');    // retorno: "Maria"
var last = list.FindLast(x => x[0] == 'M'); // retorno: "Marcos"
var exact = list.Find(x => x == "Bob");     // retorno: "Bob"
```

## 11. `FindIndex(expression)` & `FindLastIndex(expression)`
Retorna um `int` com o indice da primeira e da ultima ocorrência, respectivamente, do item que satisfaz a `expression`.  
```c#
List<string> list = new List<string>() { "Maria", "Alex", "Bob", "Ana", "Marcos" };
int first = list.FindIndex(x => x[0] == 'M');    // retorno: 0
int last = list.FindLastIndex(x => x[0] == 'M'); // retorno: 4
int exact = list.FindIndex(x => x == "Bob");     // retorno: 2
```

## 12. `FindAll(expression)`
Retorna uma lista com os elementos que satisfazem a `expression`.  
```c#
List<string> list = new List<string>() { "Maria", "Alex", "Bob", "Ana", "Marcos" };
var newList = list.FindAll(x => x[0] == 'M');
// newList = { "Maria", "Marcos" }

var newList2 = list.FindAll(x => x.Length == 3);
// newList2 = { "Bob", "Ana" }
```

## 13. `Remove(item)`
Remove o elemento passado como argumento
```c#
List<string> list = new List<string>() { "Maria", "Alex", "Bob", "Ana" };
// list = { "Maria", "Alex", "Bob", "Ana" }
list.Remove("Maria");
//list = { "Alex", "Bob", "Ana" }
```

## 14. `RemoveAt(index)`
Remove o elemento pelo indice
```c#
List<string> list = new List<string>() { "Maria", "Alex", "Bob", "Ana" };
// list = { "Maria", "Alex", "Bob", "Ana" }
list.RemoveAt(2); // remove o elemento do indice 2
//list = { "Maria", "Alex", "Ana" }
```

## 15. `RemoveRange(index, count)`
Remove uma faixa de elementos.
- `index` -> indice que começa a contagem
- `count` -> quantidade de elementos a serem removidas

```c#
List<string> list = new List<string>() { "Maria", "Alex", "Bob", "Ana", "Marcos" };
// list = { "Maria", "Alex", "Bob", "Ana", "Marcos" }
list.RemoveRange(1, 3); // remove 3 elementos a partir do indice 1
// list = { "Maria", "Marcos" }
```

## 16. `RemoveAll(expression)`
Remove o itens que satisfazem a `expression`.  
```c#
List<string> list = new List<string>() { "Maria", "Alex", "Bob", "Ana", "Marcos" };
// list = { "Maria", "Alex", "Bob", "Ana", "Marcos" };
list.RemoveAll(x => x[0] == 'M');
// list = { "Alex", "Bob", "Ana" }
```

## 17. `Clear()`
Limpa a lista deixando-a vazia
```c#
List<int> list = new List<int>() { 0, 2, 5, 5, 3, 8, 5};
list.Clear();
```
