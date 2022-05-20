# Strings

---
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
---
## Comparação

### 1. CompareTo
```c#
string text = "Some text";
Console.WriteLine(text.CompareTo("Some text"));  // retorna 0 -> iguais
Console.WriteLine(text.CompareTo("Other text")); // retorna 1 -> diferentes
```

### 2. Contains
Verifica se uma `string` contém o parametro passado na função `Contains(param)`.
Podemos usar esse metodo para comparar strings.
```c#
string text = "Some text";
Console.WriteLine(text.Contains("text"));   // true
Console.WriteLine(text.Contains("Text"));   // false
Console.WriteLine(text.Contains("other"));  // false
// ignorando o case sensitive(diferenciação entre maiusculas e minusculas)
Console.WriteLine(text.Contains("Text", StringComparison.OrdinalIgnoreCase));// true
// Comparando duas strings
Console.WriteLine(text.Contains("Some text")); // true
```
### 3. StartsWith & EndsWith
Verifica se a `string` começa ou termina com o parametro informado.
```c#
string text = "Some text";
Console.WriteLine(text.StartsWith("Some"));   // true
Console.WriteLine(text.StartsWith("some"));   // false
Console.WriteLine(text.StartsWith(" Some"));  // false
Console.WriteLine(text.StartsWith(" other")); // false

Console.WriteLine(text.EndsWith("text"));   // true
Console.WriteLine(text.EndsWith("Text"));   // false
Console.WriteLine(text.EndsWith("text "));  // false
Console.WriteLine(text.EndsWith(" other")); // false
```
### 4. Equals
Verifica se uma `string` é **exatamente** igual à outra.
Retorna `tru` se as strings forem **iguais**, caso contrário retorna `false`.

```c#
string text = "Some text";
Console.WriteLine(text.Equals("Some text"));    // true
Console.WriteLine(text.Equals("some text"));    // false
Console.WriteLine(text.Equals("Some text "));   // false
Console.WriteLine(text.Equals(" Some text "));  // false
Console.WriteLine(text.Equals("some text", StringComparison.OrdinalIgnoreCase));  // true
```
---
## Manipulação

### 1. IndexOf e LastIndexOf
```c#
string text = "Some text";

//Retorna o indice da PRIMEIRA ocorrência do parametro passado.
Console.WriteLine(text.IndexOf("o"));   // 1

// retorna o indice da ULTIMA ocorrencia do parametro passado
Console.WriteLine(text.LastIndexOf("t")); // 8
```

### 2. ToUpper & ToLower
Converte a `string` em maiusculo e minisculo
```c#
string text = "SoME tExT";
Console.WriteLine(text.ToUpper());  // "SOME TEXT"
Console.WriteLine(text.ToLower());  // "some text"
```
### 3. Insert
Insere um `char`/`string` numa posição especifica da string.
```c#
string text = "Some text";
Console.WriteLine(text.Insert(4, "INSERT"));
Console.WriteLine(text.Insert(8, "X"));
```
### 4. Remove
Remove caracteres da string. Para isso devemos passar por parametro o indice e a quantidade de caracteres a serem removidos
```c#
string text = "SomREMOVEe text";
Console.WriteLine(text.Remove(3, 6));
```
### 5. Replace
```c#
string text = "Some text";
Console.WriteLine(text.Replace("Some", "Other"));
Console.WriteLine(text.Replace("t", "X"));
```
### 6. Split
Separa a `string` pelo caractere passado por parametro criando uma lista. Geralmente esse caractere é o espaço ou a virgula.
```c#
string text = "Some text";
string[] textArray = text.Split(" ");
Console.WriteLine(textArray[0]);
Console.WriteLine(textArray[1]);
```
### 7. Substring
Recebe 2 parametros:
- o primeiro é o indice
- o segundo é quantidade de caracteres.
```c#
string text = "Some text";
string subText = text.Substring(5, 4);
Console.WriteLine(subText); // retorna "text"
```
### 8. Trim
Remove os espaços do inicio e do final da string
```c#
string text = "                 Some text       ";
Console.WriteLine(text.Trim());
```
---
## String Builder
```c#
var text = new StringBuilder();
text.Append("Some text");
text.Append("Some text");
text.Append("Some text");
text.Append("Some text");
text.Append("Some text");
Console.WriteLine(text);
```
