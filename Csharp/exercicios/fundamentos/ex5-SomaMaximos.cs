
namespace Praticando
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Escreva uma função que receba como entrada uma lista de números inteiros 
            (tamanho mínimo da lista de 3 elementos) e retorna soma dos dois maiores
            valores na lista. 
            Por exemplo, CalculaMaximo({4,3,6,1,2}) deve retornar 10 (6+4).
            */

            List<int> numeros = new List<int>() { 4, 3, 6, 1, 2 };
            Console.WriteLine(CalculaMaximo(numeros));
        }

        public static int CalculaMaximo(List<int> numeros)
        {
            int soma, max1, max2;

            max1 = numeros.Max();
            numeros.Remove(max1);
            max2 = numeros.Max();

            soma = max1 + max2;

            return soma;
        }
    }
}