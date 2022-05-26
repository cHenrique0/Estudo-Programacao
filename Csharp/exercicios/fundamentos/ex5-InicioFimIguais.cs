
namespace Praticando
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Escreva uma função que receba como entrada uma lista de palavras e retorne
            a quantidade de palavras da lista que possuem 2 ou mais caracteres e cujos
            primeiro e últimos caracteres sejam iguais. 
            Por exemplo: 
                PalavrasInicioFimIguais({ 'aba', 'xyz', 'aa', 'x', 'bbb' }) retorna 3.
            */

            List<string> palavras = new List<string>() { "aba", "xyz", "aa", "x", "bbb" };
            Console.WriteLine(PalavrasInicioFimIguais(palavras));
            
        }

        public static int PalavrasInicioFimIguais(List<string> palavras)
        {
            List<string> quantPalavras;
            quantPalavras = palavras.FindAll(x => (x.Length >= 2) && (x[0] == x[x.Length-1]));
            return quantPalavras.Count;
        }
    }
}