## Enums

- Usado para fornercer uma melhor visualização do código;
- Substituem o uso de _inteiros_;
- Usados em listas curtas;
- Usado em dados fixos;
- Sempre em **maiúsculo**
    - Começa com a letra `E`;

```c#
// Criando um Enum
enum EEstadoCivil {
    // enumeradores
    Solteiro = 1,
    Casado = 2,
    Divorciado = 3
}

// Usando um Enum
struct Cliente {
    public string Nome;
    public EEstadoCivil EstadoCivil;
}

var cliente = new Cliente("João Silva", EEstadoCivil.Casado);
Console.WriteLine(cliente.Nome);
Console.WriteLine(cliente.EstadoCivil); // imprime 'Casado'
Console.WriteLine((int)cliente.EstadoCivil); // imprime 2
```