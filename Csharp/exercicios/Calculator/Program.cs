#nullable disable

namespace Calculator {
    class Program {
        static void Main(string[] args) {

            // Limpa a tela
            Console.Clear();
            Console.WriteLine("Starting Calculator...");
             // Espera 2 segundos
            Thread.Sleep(2000);
            Console.Clear();
            
            Menu();
            
        }

        static float Soma(float num1, float num2) {
            float result = num1 + num2;
            return result;
        }

        static float Subtracao(float num1, float num2) {
            float result = num1 - num2;
            return result;
        }

        static float Multiplicacao(float num1, float num2) {
            float result = num1 * num2;
            return result;
        }

        static float Divisao(float num1, float num2) {
            float result = num1 / num2;
            return result;
        }

        static void Menu() {

            Console.WriteLine("+----------------------------+");
            Console.WriteLine("|            Menu            |");
            Console.WriteLine("+----------------------------+");
            Console.WriteLine("|       [1] - Soma           |");
            Console.WriteLine("+----------------------------+");
            Console.WriteLine("|       [2] - Subtração      |");
            Console.WriteLine("+----------------------------+");
            Console.WriteLine("|       [3] - Divisão        |");
            Console.WriteLine("+----------------------------+");
            Console.WriteLine("|       [4] - Multiplicação  |");
            Console.WriteLine("+----------------------------+");
            Console.WriteLine("|       [0] - Sair           |");
            Console.WriteLine("+----------------------------+");

            Console.Write("Escolha uma opção: ");
            short op = short.Parse(Console.ReadLine());
            switch (op) {
                case 0:
                    Console.Clear();
                    Console.WriteLine("Exiting...");
                    Thread.Sleep(2000);
                    Console.Clear();
                    break;
                case 1:
                    Console.Clear();
                    Console.WriteLine("=========== SOMA ===========");
                    float[] entradaSum = Entrada();
                    float sum = Soma(entradaSum[0], entradaSum[1]);
                    Console.WriteLine($"\n> Resultado = {sum}");
                    Console.WriteLine("\nPress [ENTER] to continue...");
                    Console.ReadKey();
                    Console.Clear();
                    Menu();
                    break;
                case 2:
                    Console.Clear();
                    Console.WriteLine("========= SUBTRAÇÃO =========");
                    float[] entradaSub = Entrada();
                    float sub = Subtracao(entradaSub[0], entradaSub[1]);
                    Console.WriteLine($"\n> Resultado = {sub}");
                    Console.WriteLine("\nPress [ENTER] to continue...");
                    Console.ReadKey();
                    Console.Clear();
                    Menu();
                    break;
                case 3:
                    Console.Clear();
                    Console.WriteLine("========= DIVISÃO =========");
                    float[] entradaDiv = Entrada();
                    float div = Divisao(entradaDiv[0], entradaDiv[1]);
                    Console.WriteLine($"\n> Resultado = {div}");
                    Console.WriteLine("\nPress [ENTER] to continue...");
                    Console.ReadKey();
                    Console.Clear();
                    Menu();
                    break;
                case 4:
                    Console.Clear();
                    Console.WriteLine("======= MULTIPLICAÇÃO =======");
                    float[] entradaMult = Entrada();
                    float mult = Multiplicacao(entradaMult[0], entradaMult[1]);
                    Console.WriteLine($"\n> Resultado = {mult}");
                    Console.WriteLine("\nPress [ENTER] to continue...");
                    Console.ReadKey();
                    Console.Clear();
                    Menu();
                    break;
                default:
                    Console.Clear();
                    Console.WriteLine("Entrada inválida!");
                    Thread.Sleep(1500);
                    Console.Clear();
                    Menu();
                    break;
            }
        }

        static float[] Entrada() {
            float[] entrada = new float[2];
            Console.Write("Digite o 1º valor: ");
            entrada[0] = float.Parse(Console.ReadLine());
            Console.Write("Digite o 2º valor: ");
            entrada[1] = float.Parse(Console.ReadLine());
            return entrada;
        }
    }
}
