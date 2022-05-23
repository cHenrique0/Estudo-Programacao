# Classe

Para representar um *"objeto"* do mundo real, usamos as **classes**.  
Uma classe é um tipo de dado em C#. Como estrutura, uma classe define os dados e o comportamento dos tipos de dados.  

## 1. Definindo uma classe
Uma classe em C# é definida usando a palavra reservada `class`.  
Por convenção, o código da classe deve ficar dentro de um arquivo com o **mesmo** nome da classe. (Se um classe for nomeada como `Aluno`, então o nome do arquivo será `Aluno.cs`).
```c#
class NomeDaClasse {
    // escopo da classe
}
```
Usando a classe:
```c#
class Program {
    static void Main(string[] args) {

        NomeDaClasse variavel = new NomeDaClasse();

    }
}
```

## 2. Membros da classe
### 2.1. Atributos
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

### 2.2. Métodos
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
### 2.3. Propriedades
São definições de métodos encapsulados, porém com uma sintaxe similar à de atributos.  

> "Uma propriedade é uma membro que oferece um mecanismo flexível para ler, gravar ou calcular o valor de um campo particular. As propriedade podem ser usadas como se fossem atributos públicos, mas na verdade elas são métodos especiais chamados "acessadores". Isso permite que os dados sejam acessados facilmente e ainda ajuda a promover a segurança e a flexibilidade dos métodos."  
> Saiba mais: [Microsoft Docs C# - Properties](https://docs.microsoft.com/pt-br/dotnet/csharp/programming-guide/classes-and-structs/properties)  

Sintaxes de uma propriedade:
```c#
class Funcionario
{
    private string _cargo;

    public string Nome { get; set; }

    public string Cargo
    {
        get { 
            return _cargo;
        }
        set { 
            _cargo = value; 
        }
    }
}
```
O acessador `get` é usado para retornar o valor da propriedade, quando o acessador `set` é usado para atribuir um novo valor.  
A palavra chave `value` é usada para definir o valor atribuído pelo acessador `set`.  
As propriedades podem ser de:
- Leitura e Gravação: possui `get` e `set`
- Somente leitura: tem apenas o `get`
- Somente gravação: tem apenas o `set`
  
Em alguns casos, os acessadores `get` e `set` da propriedade apenas atribuem ou recuperam um valor sem incluir nenhuma lógica adicional.  
A propriedade `Nome` é uma forma simplificada de definir uma propriedade e é chamada de Propriedade Auto-implementada.  

Usando as propriedades:
```c#
class Program
{
    static void Main(string[] args)
    {
        Funcionario funcionario = new Funcionario();

        // Atribuição de propriedade
        funcionario.Nome = "Jorge Silva";

        // Lendo a propriedade
        Console.WriteLine(funcionario.Cargo);
    }
}
```
A atribuição de propriedade acima faz com que o acessador `set` seja chamado.  
Ao mostrar a propriedade no console, o acessador `get` é chamado.  
** No exemplo acima a `"Jorge Silva"` é o `value`.   

#### Outra sintaxe para propriedades
Os acessadores geralmente consistem em instruções de uma única linha que simplesmente atribuem ou retornam o resultado de uma expressão.  
Podemos usar então um *expression body* com o simbolo `=>`.  
```c#
class Pessoa
{

    private string _primeiroNome;
    private string _ultimoNome;
    private int _idade;

    public string Nome => $"{_primeiroNome} {_ultimoNome}";

    public string Idade
    {
        get => _idade;
        set => _idade = value;
    }
}
```
Propriedades de somente leitura podem implementar o acessador `get` como uma expressão. Nesse caso, nem a o acessador `get` nem a palavra-chave `return` é usada.
O exemplo acima implementa a propriedade `Nome` como somente leitura e usando uma expressão.

## 3. Sobrecarga
### 3.1 Sobrecarga de construtores
É um recurso que uma classe possui para oferecer mais de uma operação com o mesmo nome, porém com diferentes listas de parâmetros.  
O construtor de um classe pode sofrer **sobrecarga**.  
Para uma classe `Produto` por exemplo:  
```c#
class Produto {

    public string Nome;
    public double Preco;
    public int Quantidade;

    // 1º metodo construtor
    public Produto() {}

    // 2º metodo construtor
    public Produto(string nome, double preco, int quantidade) {
        Nome = nome;
        Preco = preco;
        Quantidade = quantidade;
    }
    
    // 3º metodo construtor
    public Produto(string nome, double preco) {
        Nome = nome;
        Preco = preco;
    }
}

class Program {
        
    static void Main(string[] args) {

        // usando o 1º construtor
        Produto p1 = new Produto();

        // usando o 2º construtor
        Produto p3 = new Produto("TV", 500.0, 10);
        
        // usando o 3º construtor
        Produto p2 = new Produto("SOFA", 1200.0);
    }
}
```
### 3.2 Sintaxe alternativa para inicializar valores de classe
Podemos usar a sintaxe abaixo para inicializar valores das classes em C#.  
Essa sintaxe só funciona se houver um construtor padrão na classe.  
Ainda com o exemplo do `Produto` acima:
```c#
// Usando uma sintaxe alternativa pro construtor
class Program {
        
    static void Main(string[] args) {

        Produto p4 = new Produto {
            Nome = "Cama King Size";
            Preco = 2000.00;
            Quantidade = 20;
        };
    }
}
```

## 4. Palavra `this`
É uma referência para o **próprio** objeto.  
Usos comuns:
- Diferenciar atributos das variáveis locais
- Referenciar um construtor em outro construtor
- Passar o próprio objeto como argumento na chamada de um método ou construtor

### 4.1 Refenciar um constutor em outro construtor
Ao fazer isso, o construtor usado também executa o construtor referenciado pela palavra `this`.
```c#
class Produto {

    public string Nome;
    public double Preco;
    public int Quantidade;

    public Produto() {
        Quantidade = 10;
    }

    public Produto(string nome, double preco) : this() {
        Nome = nome;
        Preco = preco;
    }

    public Produto(string nome, double preco, int quantidade) : this(nome, preco) {
        Quantidade = quantidade;
    }
}
```

## 5. Modificadores de acesso

Todos os tipos e membros de tipos possuem um nível de acessibilidade. Este nivel controla se eles podem ser usados em outro código do assembly<sup>[[1]](#nota1)</sup> ou em outros assemblies diferentes.  
Para especificar a acessibilidade de um tipo ou membro podemos usar os seguintes modificadores:
- `public`: o tipo ou membro pode ser acessado por qualquer outro código no mesmo assembly ou outro assembly que faça referência a ele. O nível de acessibilidade de membros públicos de um tipo é controlado pelo nível de acessibilidade do próprio tipo.
- `private`: o tipo ou membro só pode ser acessado por código na mesma `class`ou `struct`
- `protected`: o tipo ou membro só pode ser acessado por código na mesma `class` ou em uma `class` derivada.
- `internal`: o tipo ou membro pode ser acessado por qualquer código no mesmo assembly, mas não por outro assembly. Ou seja, tipos ou membros `internal` podem ser acessados no código que faz parte da mesma compilação.
- `protected internal`: o tipo ou membro pode ser acessado por qualquer código no assembly no qual ele é declarado.
- `private protected`: o tipo ou membro pode ser acessado por tipos derivados da `class` que são declarados dentro do assembly que a contém.

<a name="nota1">[1]</a>: um assembly é um `.dll` ou `.exe` criado pela compilação de um ou mais arquivos `.cs` numa única compilação.

> Saiba mais: [Microsoft Docs C# - Access Modifiers](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/access-modifiers)

Tabela de resumo:

&nbsp;   | Própria classe | subclasse no assembly | classes do assembly | subclasses fora do assembly | classes fora do assembly
:------: | :------: | :------: | :------: | :------: | :------:
`public` | x | x | x | x | x
`private` | x
`protected` | x | x | &nbsp; | x | &nbsp;
`internal` | x | x | x | &nbsp; | &nbsp;  
`protected internal` | x | x | x | x | &nbsp;
`private protected` | x | x | &nbsp; | &nbsp; | &nbsp;


## Ordem sugeridade para implementação de membros da classe

1. Atributos privados
2. Pripriedade autoimplementadas
3. Construtores
4. Propriedades customizadas
5. Outros métodos da classe
