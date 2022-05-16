namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Um Posto de combustíveis deseja determinar qual de seus produtos tem a 
            preferência de seus clientes. Escreva um algoritmo para ler o tipo de 
            combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 
            3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa 
            de 1 a 4) deve ser solicitado um novo código (até que seja válido). 
            O programa será encerrado quando o código informado for o número 4. 
            Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes 
            que abasteceram cada tipo de combustível, conforme exemplo.
            */
            
            int combustivel = 0;
            int alcool = 0, gasolina = 0, diesel = 0;

            Menu();
            combustivel = int.Parse(Console.ReadLine());

            while (combustivel != 4) {
                if (combustivel == 1)
                    alcool++;
                else if (combustivel == 2)
                    gasolina++;
                else if (combustivel == 3)
                    diesel++;
                else {
                    Console.WriteLine("Opção inválida.");
                    Console.WriteLine();
                }
                Menu();
                combustivel = int.Parse(Console.ReadLine());
            }

            Console.WriteLine("Muito Obrigado");
            Console.WriteLine($"Alcool: {alcool}");
            Console.WriteLine($"Gasolina: {gasolina}");
            Console.WriteLine($"Diesel: {diesel}");

        }

        static void Menu() {
            Console.WriteLine("Escolha uma opção:");
            Console.WriteLine("1 - Alcool");
            Console.WriteLine("2 - Gasolina");
            Console.WriteLine("3 - Diesel");
            Console.WriteLine("4 - Sair");
            Console.WriteLine();
            Console.Write("> ");
        }
    }
}
