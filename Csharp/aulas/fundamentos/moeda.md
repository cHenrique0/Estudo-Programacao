# Representando moedas

Para representar moedas usamos o tipo de dado `decimal` por ter maior precisão que os tipos `float` e `double`.  

```c#
class Program
{
    static void Main(string[] args)
    {
        decimal valor = 10.55m;
        Console.WriteLine(
            valor.ToString(
                "C", 
                CultureInfo.CreateSpecificCulture("pt-BR")
            )
        );
    }
}
```
> Output: R$ 10,55

O _formatador_ "C" combinado com o argumento do método `CreateSpecificCulture(string culture)` retorna uma `string` formatada de acordo com o idioma(`culture`) passado.

Alguns formatadores:
- `G`: formatador númerico - especifica o tipo como um número
- `C`: (Currency = moeda) - retorna o tipo da moeda de acordo com o idoma(R$ para real, etc)
- `E04`: notação cientifica
- `F`
- `N`
- `P`

Alguns idiomas:
- `en-US`: Inglês dos Estados Unidos
- `en-UK`: Inglês Britanico
- `es-ES`: Espanhol da Espanha
- `pt-PT`: Português de Portugal
- etc
