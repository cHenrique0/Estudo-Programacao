namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares 
            de 1 até X, um valor por linha, inclusive o X, se for o caso.
            */

            Console.Write("Digite um número inteiro entre 1 e 1000: ");
            int x = int.Parse(Console.ReadLine());

            for(int i = 1; i <= x; i++) {
                if(i % 2 !=  0) {
                    Console.WriteLine(i);
                }
            }

        }
    }
}
