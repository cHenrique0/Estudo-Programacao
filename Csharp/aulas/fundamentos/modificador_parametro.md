# Modificador de parâmetros

## 1. `params`

Usando a palavra-chave `params`, podemos especificar parâmetros que recebem um número variável de argumentos. O tipo de parâmetro **deve** ser um array unidimensional.  
Em uma declaração de método, apenas **um** `params` é permitido e enhum parâmetro adicional é permitido após `params`.

Ao chamar um método com um parâmetro `params`, podemos passar:
- Uma lista separada por vírgula como argumentos, do tipo dos elementos do array.
- Um array de argumentos do tipo especificado.
- Ou não passar argumentos. Nesse caso o comprimento da lista `params` será zero.

Exemplo:
```c#
class Program
{
    static void Main(string[] args)
    {
        // passando varios argumentos separados por virgula
        Console.WriteLine(Sum(1, 2, 3)); // retorno: 6
        Console.WriteLine(Sum(1, 2, -3, 4)); // retorno: 4

        // passando um array do mesmo tipo como argumento
        double[] array = {1, 2, 3, 4};
        Console.WriteLine(Sum(array)); // retorno: 10

        // Nenhum argumento
        Console.WriteLine(Sum()); // retorno: 0

    }
    
    public static double Sum(params double[] numeros)
    {
        double sum = 0;
        foreach (var num in numeros)
        {
            sum += num;
        }

        return sum;
    }
}
```
## 2. `ref`


## 3. `out`
