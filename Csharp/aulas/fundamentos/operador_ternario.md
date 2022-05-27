# Expressão condicional ternária

É uma estrutura **opicional** ao `if-else` quando se deseja decidir um _valor_ com base em uma condição.  
A expressão condicional ternária é definida pelo operador `?:`.  

Sintaxe:
> (condição) ? valorCasoVerdadeiro : valorCasoFalso

Exemplo:
```c#
int number = (2 > 4) ? 50 : 80; // 80
string name = (10 != 3) ? "Maria" : "Alex"; // "Maria"
```