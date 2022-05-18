# Entrada de dados:

## 1. A partir do Teclado:

Ler dados informado pelo usuário a partir do teclado

```c#
// Lendo a entrada até a primeira quebra de linha
string frase = Console.ReadLine();

// separando a entrada pelo espaço
string[] vetor = Console.ReadLine().Split(' '); // exemplo de entrada: Vermelho Verde Azul
string a = vetor[0];
string b = vetor[1];
string c = vetor[2];
```