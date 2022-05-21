namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Faça um programa para ler dois valores inteiros, e depois mostrar na tela 
            a soma desses números.
            */

            Console.WriteLine("Digite 2 números inteiros:");
            Console.Write("1°: ");
            int num_1 = int.Parse(Console.ReadLine());
            Console.Write("2°: ");
            int num_2 = int.Parse(Console.ReadLine());

            int sum = num_1 + num_2;

            Console.WriteLine($"Soma = {sum}");

        }
    }
}
