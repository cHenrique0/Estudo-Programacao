## Conversões

## 1. Conversão Implícita

- É comum precisarmos transformar um dado do tipo X para tipo Y;
- Existem dois tipos de conversão, as implicitas e as explicitas;
- As conversões implicitas:
    - Podem ser executadas apenas com passagem de dados;
    - Possuem tipos compatívies;

```c#
float value = 25.8F;
int other = 25;
value = other;  // Conversão implicita
other = value;  // ERRO!
```

- A conversão acima ocorreu pois um número real pode receber um número inteiro;
- Ao contrátio não aconteceria;
    - Um número inteiro não tem pontuação, logo ele não poderia receber um número real;
- A conversão implicita só ocorrerá se:
    - O tipo de dado for compatível;
    - O tamanho do dado for compativel;
- Em caso de números, a precisão pode ser alterada;
- Qualquer situação adversa causará erro;

Tipo | Conversão
 :------: | :------:
sbyte | short, int, long, float, double, decimal
byte | short, ushort, int, uint, long, ulong, float, double, decimal
short | int, long, float, double, decimal
ushort | int, uint, long, ulong, float, double, decimal
int | long, float, double, decimal
uint | long, ulong, float, double, decimal
long | float, double, decimal
ulong | float, double, decimal
char | ushort, int, uint, longe, ulong, float, double, decimal
float | double

## 2. Conversão Explícita

- Ocorre quando os tipos não são compatíveis;
- É dada pelo uso do tipo entre parênteses antes da atribuição;
- Segue as mesmas regras da Conversão Implicita;

```c#
int integer = 100;
uint unsiged_integer = (uint)integer;   // Conversão explícita
```

## 3. Parse

- Método presente em todo tipo primitivo(bult-in);
- **Usado para converter um `char` ou `string` para um tipo qualquer**;
- Caso haja alguma incompatibilidade, gera um erro;

```c#
int integer = int.Parse("100");     // Convertendo uma string em int
```

## 4. Convert

- Similar ao parse;
- Permite converter vários tipos;
- Devemos informar o tipo na chamada da conversão;

```c#
int integer = Convert.ToInt32("100");
```

