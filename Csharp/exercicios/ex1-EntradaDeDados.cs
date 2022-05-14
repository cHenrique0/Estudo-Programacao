namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Faça um programa para executar um interação com o usuário, lendo os 
            valores e mostrando os dados na tela.
            */

            Console.WriteLine("Digite seu nome completo:");
            string nome = Console.ReadLine();

            Console.WriteLine("Quantos quartos tem na sua casa?");
            int quartos = int.Parse(Console.ReadLine());

            Console.WriteLine("Digite o preço de um produto:");
            double valor = double.Parse(Console.ReadLine());

            Console.WriteLine("Digite seu último nome, idade e altura(na mesma linha, separado por espaço):");
            string[] infos = Console.ReadLine().Split(' ');
            string ultimoNome = infos[0];
            int idade = int.Parse(infos[1]);
            double altura = double.Parse(infos[2]);

            Console.WriteLine("Você digitou:");
            Console.WriteLine(nome);
            Console.WriteLine(quartos);
            Console.WriteLine(valor);
            Console.WriteLine(ultimoNome);
            Console.WriteLine(idade);
            Console.WriteLine(altura);
        }
    }
}