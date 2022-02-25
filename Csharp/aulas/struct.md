## Struct

- Tipos de dados estruturado;
- Apenas a estrutura, o esqueleto;
- **Value Type**;
- Armazenam apenas outros tipos de dados;
- Definido pela palavra `struct`;
- Composto de propriedades e métodos;
- O nome sempre com letra maiscula;
    - O mesmo para propriedades e métodos;
- Criado a partir da palavra `new`;

```c#
// Criando a struct
struct Product
{
    // Properties
    public int Id;
    public decimal Price;
    public string Title;

    // Construtor method
    // Recebe o mesmo nome da struct
    public Product(int id, string title, float price){
        Id = id;
        Title = title;
        Price = price;
    }

    // Methods
    public float PriceInDolar(decimal dolar){
        return Price * dolar;
    }
}

// Usando a struct
static void Main(string[] args)
{
    var product = new Product(1, "Algum titulo", 4.55m);
}
```