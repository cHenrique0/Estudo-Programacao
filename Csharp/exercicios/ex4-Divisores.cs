namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Ler um número inteiro N e calcular todos os seus divisores.
            */

            int N = 0;

            Console.Write("Digite um número inteiro: ");
            N = int.Parse(Console.ReadLine());

            for(int i = 1; i <= N; i++){
                if(N % i == 0) {
                    Console.WriteLine(i);
                }
            }
        }
    }
}
