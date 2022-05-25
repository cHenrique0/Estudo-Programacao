
namespace Praticando
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Escreva uma função que receba uma lista de números inteiros e retorne 
            a soma dos números ímpares na lista. 
            Por exemplo, SomaImpares({ 11, 20, 36, 41, 55, 6 }) deve retornar 107.
            */

            List<int> numeros = new List<int>() { 11, 20, 36, 41, 55, 6 };
            Console.WriteLine(SomaImpares(numeros));
        }

        public static int SomaImpares(List<int> numeros)
        {
            int soma = 0;
            
            foreach (var item in numeros)
            {
                if(item % 2 != 0)
                {
                    soma += item;
                }
            }

            return soma;
        }
    }
}