namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Ler um valor N. Calcular e escrever seu respectivo fatorial. 
            Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.
            Lembrando que, por definição, fatorial de 0 é 1.
            */

            int N = 0;
            int fatorial = 1;

            Console.Write("Digite um número inteiro positivo: ");
            N = int.Parse(Console.ReadLine());

            for(int i = 1; i <= N; i++) {
                fatorial *= i;
            }

            Console.WriteLine($"fatorial = {fatorial}");
        }
    }
}
