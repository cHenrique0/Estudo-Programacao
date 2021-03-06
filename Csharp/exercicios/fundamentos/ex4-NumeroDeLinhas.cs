namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Fazer um programa para ler um número inteiro positivo N. O programa deve 
            então mostrar na tela N linhas, começando de 1 até N. Para cada linha, 
            mostrar o número da linha, depois o quadrado e o cubo do valor, conforme exemplo.

            Entrada:    Saída:
            5           1 1 1
                        2 4 8
                        3 9 27
                        4 16 64
                        5 25 125
            */

            int N = 0;

            Console.Write("Digite um número inteiro: ");
            N = int.Parse(Console.ReadLine());

            for(int i = 1; i <= N; i++){
                Console.WriteLine($"{i} {i*i} {i*i*i}");
            }
        }
    }
}
