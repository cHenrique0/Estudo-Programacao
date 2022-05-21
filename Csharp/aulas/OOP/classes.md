# Classe

Para representar um *"objeto"* do mundo real, usamos as **classes**.  
Uma classe é um tipo de dado em C#. Como estrutura, uma classe define os dados e o comportamento dos tipos de dados.  
---
## Definindo uma classe
Uma classe em C# é definida usando a palavra reservada `class`.  
Por convenção, o código da classe deve ficar dentro de um arquivo com o **mesmo** nome da classe. (Se um classe for nomeada como `Aluno`, então o nome do arquivo será `Aluno.cs`).
```c#
class NomeDaClasse {
    // escopo da classe
}
```
Usando a classe:
```c#
class Programa {
    NomeDaClasse variavel = new NomeDaClasse();
}
```
---
## Atributos, métodos, propriedades
### 1. Atributos
Dentro de uma classe queremos armazenar informações que descrevem o **objeto**.  
Para isso fazemos declarações de variáveis dentro do escopo da classe.  
Essas variáveis são chamadas de **atributos**.  
Em uma classe `Carro` podemos dizer que `cor`, `peso` e `modelo` são seus atributos.  

Declarando atributos:
```c#
class Carro {
    public string cor;
    public double peso;
    public string modelo;
}
```
** O uso da palavra reservada `public` serve para que a aplicação leia e escreva nesses atributos.

### 2. Métodos
Métodos definem através de rotinas as ações que um objeto venha a apresentar.  
Ainda no exemplo da classe `Carro` poderia ter os métodos: acelerar, frear e ligar.

Métodos são funções e devem ser declaradas como tal:
```c#
class Carro {
    public string Cor;
    public double Peso;
    public string Modelo;

    public void Frear() {
        // escopo do método
    }

    public void Acelerar() {
        // escopo do método
    }

    public void Ligar() {
        // escopo do método
    }
}
```

Dentro dos métodos existe um em especial. Ele é chamado de **Construtor**.  
O método construtor é sempre chamado quando se cria um novo objeto, ele pode ou não conter uma assinatura(declaração).
```c#
class NomeDaClasse {
    
    // atributos

    // Construtor
    public NomeDaClasse(parametros) {
        // implementação do construtor
        // geralmente é atribuição dos parametros aos respectivos atributos da classe
    }

    // outros métodos
}
```