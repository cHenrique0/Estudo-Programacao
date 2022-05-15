namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Faça um programa para ler o valor do raio de um círculo, e depois mostrar 
            o valor da área deste círculo com quatro casas decimais.
            
            - Fórmula da área: area = π . raio^2
            - Considere o valor de π = 3.14159
            */

            Console.Write("Digite o valor do raio do circulo: ");
            double raio = double.Parse(Console.ReadLine());

            double area = 3.14159 * Math.Pow(raio, 2);

            Console.WriteLine($"Area = {area:F4}");

        }
    }
}
