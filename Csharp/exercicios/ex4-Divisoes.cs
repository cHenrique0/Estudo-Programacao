namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Fazer um programa para ler um número N. Depois leia N pares de números e mostre
            a divisão do primeiro pelo segundo. Se o denominador for igual a zero, 
            mostrar a mensagem "divisao impossivel".
            */

            int N = 0;
            string[] numeros;
            double divisao = 0.0;

            Console.Write("Quantas divisões você quer fazer? ");
            N = int.Parse(Console.ReadLine());

            for(int i = 1; i <= N; i++) {
                Console.Write("Digite o par de números(ex.: 9 3): ");
                numeros = Console.ReadLine().Split(' ');
                double num1 = double.Parse(numeros[0]);
                double num2 = double.Parse(numeros[1]);

                if (num2 == 0.0) {
                    Console.WriteLine("Divisão impossivel");
                }
                else {
                    divisao = num1 / num2;
                    Console.WriteLine($"{divisao}");
                }

            }
        }
    }
}
