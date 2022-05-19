# Strings

## Formatação

### 1. Concatenação
Junta strings em uma única string.
Ao concatenar, ocorre uma conversão automatica dos tipos para string
```c#
var price = 10.2;
var text = "The product price is " + price;
Console.WriteLine(text); // The product price is 10.2;
```

### 2. Format
Usando a função `string.Format` podemos interpolar uma string.
Os parametros são: uma string e os valores a serem interpolado.
Usa-se `{número}` na string, cada número será substituido pelo *valor* correspondente,
começando a contagem no **primeiro** valor informado após a `string`.

No exemplo abaixo, a chave `{0}` na string será substituida pelo valor `price`.
```c#
var price = 10.2;
var text = string.Format("The product price is {0}", price);
Console.WriteLine(text);
```

### 3. Interpolação com $

O uso é semelhante ao `string.Format` mas possui uma outra particularidade.
Com o `$` para formatar strings podemos informar os valores direto na string.
```c#
var price = 10.2;
Console.WriteLine($"The product price is {price}");
```
