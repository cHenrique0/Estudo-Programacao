namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Com base na tabela abaixo, escreva um programa que leia o código de 
            um item e a quantidade deste item. 
            A seguir, calcule e mostre o valor da conta a pagar.

            +--------+--------------+---------+ 
            | Codigo |     Item     |  Preço  |
            +--------+--------------+---------+
            |   1    |   Hot-dog    | R$ 4.00 |
            +--------+--------------+---------+
            |   2    |   X-Salada   | R$ 4.50 |
            +--------+--------------+---------+
            |   3    |   X-Bacon    | R$ 5.00 |
            +--------+--------------+---------+
            |   4    |   Torrada    | R$ 2.00 |
            +--------+--------------+---------+
            |   5    | Refrigerante | R$ 1.50 |
            +--------+--------------+---------+
            */

            int cod, qtd;
            double preco = 0;

            Console.Write("Digite o codigo do item e a quantidade(separados por espaços): ");
            string[] entrada = Console.ReadLine().Split(" ");
            
            cod = int.Parse(entrada[0]);
            qtd = int.Parse(entrada[1]);

            if(cod == 1)
                preco = qtd * 4.00;
            else if(cod == 2)
                preco = qtd * 4.50;
            else if(cod == 3)
                preco = qtd * 5.00;
            else if(cod == 4)
                preco = qtd * 2.00;
            else if(cod == 5)
                preco = qtd * 1.50;
            else
                Console.WriteLine("Codigo inválido");
            
            Console.WriteLine($"Total: R$ {preco:F2}");

        }
    }
}
