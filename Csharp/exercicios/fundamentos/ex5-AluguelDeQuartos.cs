
namespace Praticando
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            A dona de um pensionato possui dez quartos para alugar para estudantes, 
            sendo esses quartos identificados pelos números 0 a 9. 
            Quando um estudante deseja alugar um quarto, deve-se registrar o nome 
            e email deste estudante.
            Fazer um programa que inicie com todos os dez quartos vazios, e depois
            leia uma quantidade N representando o número de estudantes que vão alugar 
            quartos (N pode ser de 1 a 10). Em seguida, registre o aluguel dos N 
            estudantes. Para cada registro de aluguel, informar o nome e email do 
            estudante, bem como qual dos quartos ele escolheu (de 0 a 9). Suponha que 
            seja escolhido um quarto vago. Ao final, seu programa deve imprimir um 
            relatório de todas ocupações do pensionato, por ordem de quarto.
            */

            Estudante[] quartos = new Estudante[10];
            Console.Write("Quantos quartos serão alugados? ");
            int quantidadeAluguel = int.Parse(Console.ReadLine());
            
            Console.WriteLine("Digite as informações do(s) estudante(s)");
            for (int i = 1; i <= quantidadeAluguel; i++)
            {
                Console.WriteLine();
                Console.WriteLine($"{i}º Aluguel");
                Console.Write("Nome: ");
                string nome = Console.ReadLine();
                Console.Write("E-mail: ");
                string email = Console.ReadLine();
                Console.Write("Quarto: ");
                int quarto = int.Parse(Console.ReadLine());
                quartos[quarto] = new Estudante(nome, email);
            }

            Console.WriteLine();
            Console.WriteLine("Quartos ocupados:");
            for (int i = 0; i < quartos.Length; i++)
            {
                if(quartos[i] != null)
                {
                    Console.WriteLine();
                    Console.WriteLine($"{i}:\n{quartos[i]}");
                }
            }

        }
    }

    class Estudante
    {
        public string Nome { get; private set; }
        public string Email { get; private set; }

        public Estudante(string nome, string email)
        {
            this.Nome = nome;
            this.Email = email;
        }

        public override string ToString()
        {
            return $"Nome: {this.Nome}\nE-mail: {this.Email}";
        }

    }
}