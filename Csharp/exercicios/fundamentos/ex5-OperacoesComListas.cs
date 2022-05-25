
namespace Praticando
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Crie uma lista chamada com os seguintes itens: 76, 92.3, “oi”, True, 4, 76
            Escreva comandos para:
            a) Inserir “laranja” e 76 no final da lista.
            b) Inserir “gato” na posição de índice 3.
            c) Inserir 99 no início da lista.
            d) Encontrar o índice de “oi”.
            e) Remover a primeira ocorrência de 76 da lista.
            */

            List<object> myList = new List<object>() { 76, 92.3, "oi", true, 4, 76 };
            myList.Add("laranja");
            myList.Insert(3, "gato");
            myList.Insert(0, 99);
            Console.WriteLine($"index of 'oi': {myList.FindIndex(x => Convert.ToString(x) == "oi")}");
            myList.Remove(76);
            
            foreach (var item in myList)
            {
                Console.WriteLine(item);
            }
        }
    }
}