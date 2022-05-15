namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Fazer um programa que leia o número de um funcionário, seu número de horas 
            trabalhadas, o valor que recebe por hora e calcule o salário desse 
            funcionário. A seguir, mostre o número e o salário do funcionário, com duas
            casas decimais.
            */

            Console.WriteLine("Digite as informações do funcionário...");
            
            Console.Write("Número do funcionário: ");
            int id = int.Parse(Console.ReadLine());

            Console.Write("Horas trabalhadas: ");
            int horas = int.Parse(Console.ReadLine());

            Console.Write("Valor da hora: ");
            double valorHora = double.Parse(Console.ReadLine());

            double salario = horas * valorHora;

            Console.WriteLine();
            Console.WriteLine($"Número = {id}");
            Console.WriteLine($"Salário = R$ {salario:F2}");

        }
    }
}
