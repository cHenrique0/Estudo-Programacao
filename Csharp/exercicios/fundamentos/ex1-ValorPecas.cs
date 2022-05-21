namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Fazer um programa para ler o código de uma peça 1, o número de peças 1, 
            o valor unitário de cada peça 1, o código de uma peça 2, o número de 
            peças 2 e o valor unitário de cada peça 2. 
            Calcule e mostre o valor a ser pago
            */

            Console.WriteLine("Digite o codigo, quantidade e valor de cada peça (separado por espaços)");
            
            Console.Write("Peça 1: ");
            string[] infos = Console.ReadLine().Split(" ");
            int cod_p1 = int.Parse(infos[0]);
            int qtde_p1 = int.Parse(infos[1]);
            double valor_p1 = double.Parse(infos[2]);

            Console.Write("Peça 2: ");
            infos = Console.ReadLine().Split(" ");
            int cod_p2 = int.Parse(infos[0]);
            int qtde_p2 = int.Parse(infos[1]);
            double valor_p2 = double.Parse(infos[2]);

            double total = (qtde_p1 * valor_p1) + (qtde_p2 * valor_p2);

            Console.WriteLine($"Valor a pagar = R$ {total:F2}");
        }
    }
}
