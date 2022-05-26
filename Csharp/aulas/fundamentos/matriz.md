# Matrizes

Na programação, **matriz** é o nome dado para _arrays bidimensionais_.  
Podemos enxergar uma matriz como uma lista de listas.  

## 1. Declarando uma matriz:
```c#
// Criando uma matriz:
tipo[,] nomeMatriz = new tipo[linha, coluna];
// linha -> tamanho da linha
// coluna -> tamanho da coluna

// Criando e inicializando a matriz
tipo[,] nomeMatriz = { { 1, 2, 3 }, {4, 5, 6 } };
```

## 2. Declarando uma matriz usando `List<T>`:
```c#
List<int>[] matriz = new List<int>[3];
matriz[0] = new List<int> { 1, 2, 3 };
matriz[1] = new List<int> { 4, 5, 6 };
matriz[2] = new List<int> { 7, 8, 9 };
```

## 3. Propriedades:
```c#
int[,] matriz = new int[3, 4];
```

### 3.1 `Length`
Retorna a quantidade de elementos da matriz
```c#
matriz.Length; // retorno: 12
```

### 3.2 `Rank`
Retorna a primeira dimensão da matriz(a quantidade de linhas)
```c#
matriz.Rank; // retorno: 3
```

### 3.3 `GetLength(dimension)`
Retorna o tamanho da `dimension` passada como argumento.  
`dimension` deve ser um `int`.  
```c#
matriz.GetLength(0); // retorno: 3
matriz.GetLength(1); // retorno: 4
```
