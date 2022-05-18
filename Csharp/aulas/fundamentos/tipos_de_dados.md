## Tipos de dados

## 1. Byte

- É utilizado para representar um byte de fato;
- Em alguns casos precisamos de cadeia de bytes de um arquivo, por exemplo;
    - Essas cadeias são chamadas de _byte array_;
- Existe também o `sbyte`, que premite valores _negativos_;

**OBS:** signed(valores com sinal) e unsigned(valores sem sinal)

- Definições:

Tipo | Bits | Capacidade
 :------: | :------: | :------:
byte | 8-bit | 0 a 255
sbyte | 8-bit | -128 a 127

```csharp
byte myByte = 127;
sbyte mySByte = -50;
```

## 2. Integer

- Números inteiros, ou seja, sem pontuação.
- Podem ser definidos pelos tipos:
    - **short/ushort:** números pequenos
    - **int/uint:** números razoáveis
    - **long/ulong:** números muito grandes
- Os inteiros, por padrão, permitem números negativos;
    - Então usa-se o **usigned** para definir que o mesmo _não_ pode receber valores negativos;
- O tipo `int` é o mais comum;

- Definições:

Tipo | Bits | Capacidade
 :------: | :------: | :------:
short | 16-bit | -32 768 a 32 767
ushort | 16-bit | 0 a 65 535
int | 32-bit | -2 147 483 648 a 2 147 483 647
uint | 32-bit | 0 a 4 294 967 295
long | 64-bit | -9 223 372 036 854 775 808 a 9 223 372 036 854 775 807
ulong | 64-bit | 0 a 18 445 744 073 709 551 615

```csharp
int idade = -265345;
uint idade = 10;
short num = 1;
ulong numero = 1255235325;
```

## 3. Floating Point

- Números que exigem uma maior precisão;
- São números com ponto flutuante, ou seja, números decimais:
    - float (Notação F);
    - double;
    - decimal (Notação M);
- Possuvem assimilação negativa e positiva por padrão, dispensando o uso do signed/unsigned em seus tipos;

- Definições:

Tipo | Bits | Capacidade
 :------: | :------: | :------:
float | 32-bit | -3.402823<sup>38</sup> a 3.402823<sup>38</sup>
double | 64-bit | -1.79769313486232<sup>308</sup> a 1.79769313486232<sup>308</sup>
decimal | 128-bit | (+ ou -)1.0x10<sup>-28</sup> a 7.9x10<sup>28</sup>

```csharp
float num1 = 2.500f;    // usar F para definir que é um tipo float
double num2 = 12.000;
decimal num3 = 25.000m; // usar M para definir um tipo decimal
var num4 = 12.33;       // o var é convertido implicitamente para double
```

## 4. Boolean

- Tipo booleano, armazena apenas `true` ou `false` (Verdadeiro ou Falso);
- Definido pela palavra reservada `bool`;

Tipo | Bits | Capacidade
 :------: | :------: | :------:
 bool | 8-bit | `true` ou `false` 

```csharp
bool userLogin = true;
bool inList = false;
```

## 5. Character

- Utilizado para armazenar **apenas** um caractere no formato Unicode;
- Definido pela palavra reservada `char`;
- A atribuição de um valor `char` é dada por aspas simples `' '`;

Tipo | Bits | Capacidade
 :------: | :------: | :------:
char | 16-bit | Qualquer caractere

```csharp
char firstLetter = 'C';
var secondLetter = 'D';
```

## 6. String

- Armazena uma cadeia de caracteres;
    - Pode ser definida como uma lista de `char`;
- Definido pela palavra reservada `string`;
- A atribuição de um valor string é dada por aspas duplas `" "`;

Tipo | Bits | Capacidade
 :------: | :------: | :------:
string | ? | uma cadeia de caracteres

```csharp
string charArray = "Some text";
string text = "My text";
var document = "0123456789";
```

## 7. Var

- Substitui o nome de um tipo;
- Será do tipo do primeiro valor atrbuído à ele;
    - Se atribuir um valor inicial do tipo `int` ao `var` ele assumira o mesmo tipo;
    - Logo, o `var` só poderá receber valores do tipo `int`;
    - O mesmo acontce com os outros tipos;

```csharp
var idade = 25;         // Será do tipo int
var nome = "André";     // Será do tipo string 
```

## 8. Object

- Tipo genérico que recebe qualquer valor ou objeto;
- Semelhante ao `var`;
- Caso não saiba o tipo da informação ou ela seja de vários tipos diferentes;
- Não possui intelisense(Ajuda do editores) por ser um tipo desconhecido;
- **Evitar o uso**;

```csharp
object quantidade;
quantidade = 32.7;
quantidade = "Some text";

object idade = 25;      // será do tipo object
object nome = "André";  // será do tipo object
```

## 8. Nullable Type

- Significa vazio, nada;
- Diferente de zero ou string vazia;
- Topo tipo, primitivo ou complexo, pode receber o valor `null`;
- O tipo deve ser marcado como _Nullable Type_;

- Podemos atribuir `null` a um objeto;
    - Desde que o  mesmo seja marcado como nullable, usando `?` após o tipo;
- Se uma chamada a um valor nulo for feita, um erro será apresentado;

```csharp
int idade1 = null;      // ERRADO!!
int? idade2 = null;      // Correto
```
