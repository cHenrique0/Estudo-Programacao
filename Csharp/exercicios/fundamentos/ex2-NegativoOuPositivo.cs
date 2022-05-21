namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Fazer um programa para ler um número inteiro, e depois dizer se este número
            é negativo ou não.
            */

            Console.Write("Digite um número inteiro: ");
            int numero = int.Parse(Console.ReadLine());

            if(numero < 0) {
                Console.WriteLine("NEGATIVO");
            }
            else {
                Console.WriteLine("POSITIVO");
            }

        }
    }
}
