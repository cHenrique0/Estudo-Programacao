namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X
            que serão lidos em seguida. Mostre quantos destes valores X estão dentro 
            do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas 
            informações conforme exemplo (use a palavra "in" para dentro do intervalo, 
            e "out" para fora do intervalo).

            Entrada:            Saida:
            5                   2 in
            14                  3 out
            123
            10
            -25
            32
            */

            int N = 0, dentro = 0, fora = 0;
            
            Console.Write("Quantos números você quer digitar? ");
            N = int.Parse(Console.ReadLine());

            for(int i = 1; i <= N; i++) {
                Console.Write($"Digite o {i}° número: ");
                int x = int.Parse(Console.ReadLine());

                if(x >= 10 && x <= 20) {
                    dentro++;
                }
            }
            fora = N - dentro;

            Console.WriteLine("Intervalo [10, 20]");
            Console.WriteLine($"{dentro} in");
            Console.WriteLine($"{fora} out");

        }
    }
}
