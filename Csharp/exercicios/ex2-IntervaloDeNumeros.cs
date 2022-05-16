namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Você deve fazer um programa que leia um valor qualquer e apresente uma
            mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], 
            (50,75], (75,100]) este valor se encontra. 
            Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser
            impressa a mensagem “Fora de intervalo”.
            */

            Console.Write("Digite um número qualquer: ");
            double valor = double.Parse(Console.ReadLine());

            if (valor < 0 || valor > 100)
                Console.WriteLine("Fora de intervalo");
            else if (valor <= 25)
                Console.WriteLine("Intervalo [0, 25]");
            else if (valor <= 50)
                Console.WriteLine("Invervalo (25, 50]");
            else if (valor <= 75)
                Console.WriteLine("Invervalo (50, 75]");
            else if (valor <= 100)
                Console.WriteLine("Invervalo (75, 100]");

        }
    }
}
