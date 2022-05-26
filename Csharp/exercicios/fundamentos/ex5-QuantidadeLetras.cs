
namespace Praticando
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Escreva uma função que receba uma lista de palavras 
            e retorne o número de palavras na lista que tenham comprimento 5. Por 
            exemplo, QuantidadeLetras5({ 'Brasil','peralta','mesa','lance','teste' }) 
            deve retornar 2.
            */

            List<string> palavras = new List<string>() { 
                "Brasil", "peralta", "mesa", "lance", "teste" 
            };

            Console.WriteLine(QuantidadeLetras5(palavras));

        }

        public static int QuantidadeLetras5(List<string> palavras)
        {
            List<string> quantPalavras = palavras.FindAll(x => x.Length == 5);

            return quantPalavras.Count;
        }
    }
}