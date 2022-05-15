namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Fazer um programa para ler quatro valores inteiros A, B, C e D. 
            A seguir, calcule e mostre a diferença do produto de A e B pelo produto 
            de C e D.
            */

            Console.WriteLine("Digite 4 valores inteiros:");
            Console.Write("1°: ");
            int A = int.Parse(Console.ReadLine());
            Console.Write("2°: ");
            int B = int.Parse(Console.ReadLine());
            Console.Write("3°: ");
            int C = int.Parse(Console.ReadLine());
            Console.Write("4°: ");
            int D = int.Parse(Console.ReadLine());

            int dif = (A * B) - (C * D);

            Console.WriteLine($"Diferença = {dif}");

        }
    }
}
