#nullable disable

namespace ex3_ContaBancaria
{
    class Program
    {
        static void Main(string[] args)
        {
            Conta conta;

            Console.WriteLine("Informe os dados do titular da conta abaixo");
            Console.Write("Número da conta: ");
            int numConta = int.Parse(Console.ReadLine());
            Console.Write("Nome do titular: ");
            string titular = Console.ReadLine();
            Console.Write("Deposito inicial (s/n)? ");
            char temDeposito = char.Parse(Console.ReadLine().ToLower());

            if(temDeposito == 's')
            {
                Console.Write("Digite o valor do depósito inicial: ");
                double valorDeposito = double.Parse(Console.ReadLine());
                conta = new Conta(numConta, titular, valorDeposito);
            }
            else {
                conta = new Conta(numConta, titular);
            }

            Console.WriteLine(conta);

            Menu();

            double valor;

            while(true)
            {
                int op = int.Parse(Console.ReadLine());
                
                switch (op)
                {
                    case 0:
                        break;
                    case 1:
                        Console.Write("\nDigite o valor do saque: ");
                        valor = double.Parse(Console.ReadLine());
                        conta.Saque(valor);
                        Console.WriteLine(conta);
                        Menu();
                        break;
                    case 2:
                        Console.Write("\nDigite o valor do depósito: ");
                        valor = double.Parse(Console.ReadLine());
                        conta.Deposito(valor);
                        Console.WriteLine(conta);
                        Menu();
                        break;
                    case 3:
                        Console.WriteLine($"\nSaldo: R$ {conta.Saldo:F2}");
                        Menu();
                        break;
                    case 4:
                        Console.WriteLine(conta);
                        Menu();
                        break;
                    default:
                        Console.WriteLine("\nDigite uma opção válida!");
                        Menu();
                        break;
                }
                
                if(op == 0)
                    break;
            }


        }

        static void Menu()
        {
            Console.WriteLine();
            Console.WriteLine("Qual operação deseja realizar? ");
            Console.WriteLine(" [1] - Saque");
            Console.WriteLine(" [2] - Deposito");
            Console.WriteLine(" [3] - Saldo");
            Console.WriteLine(" [4] - Dados da conta");
            Console.WriteLine(" [0] - Sair ");
            Console.Write("> ");
        }
    }
}