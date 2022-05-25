
namespace Praticando
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Escreva uma função que receba uma lista de números e retorne a soma 
            dos quadrados dos números na lista.
            Por exemplo, SomaQuadrados({ 2, 3, 4 }) deve retorna 4+9+16 que é 29.
            */

            List<int> numeros = new List<int>() { 2, 3, 4 };
            Console.WriteLine(SomaQuadrados(numeros));
            
        }

        public static double SomaQuadrados(List<int> numeros)
        {
            double soma = 0;

            foreach (var item in numeros)
            {
                soma += Math.Pow(item, 2);
            }

            return soma;
        }
    }
}