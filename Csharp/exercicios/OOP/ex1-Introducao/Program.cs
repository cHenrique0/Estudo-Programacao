#nullable disable

namespace ex1_Introducao {
    class Program {
        static void Main(string[] args) {
            
            /* Primeiro exercicio:
            Fazer um programa para ler os dados de duas pessoas, depois mostrar o 
            nome da pessoa mais velha.
            */

            /*
            Pessoa pessoa1 = new Pessoa();
            Pessoa pessoa2 = new Pessoa();

            Console.WriteLine("Dados da primeira pessoa: ");
            Console.Write("Nome: ");
            pessoa1.Nome = Console.ReadLine();
            Console.Write("Idade: ");
            pessoa1.Idade = int.Parse(Console.ReadLine());

            Console.WriteLine("Dados da segunda pessoa: ");
            Console.Write("Nome: ");
            pessoa2.Nome = Console.ReadLine();
            Console.Write("Idade: ");
            pessoa2.Idade = int.Parse(Console.ReadLine());

            if(pessoa1.Idade > pessoa2.Idade) {
                Console.WriteLine($"Pessoa mais velha: {pessoa1.Nome}");
            }
            else if(pessoa2.Idade > pessoa1.Idade) {
                Console.WriteLine($"Pessoa mais velha: {pessoa2.Nome}");
            }
            */

            /* Segundo exercicio:
            Fazer um programa para ler nome e salário de dois funcionários. 
            Depois, mostrar o salário médio dos funcionários.
            */

            Funcionario funcionario1 = new Funcionario();
            Funcionario funcionario2 = new Funcionario();
            double salarioMedio = 0.0;

            Console.WriteLine("Dados do primeiro funcionario: ");
            Console.Write("Nome: ");
            funcionario1.Nome = Console.ReadLine();
            Console.Write("Salario: ");
            funcionario1.Salario = double.Parse(Console.ReadLine());

            Console.WriteLine("Dados do segunda funcionario: ");
            Console.Write("Nome: ");
            funcionario2.Nome = Console.ReadLine();
            Console.Write("Salario: ");
            funcionario2.Salario = double.Parse(Console.ReadLine());

            salarioMedio = (funcionario1.Salario + funcionario2.Salario) / 2;

            Console.WriteLine($"Salário médio = {salarioMedio:F2}");

        }
    }
}
