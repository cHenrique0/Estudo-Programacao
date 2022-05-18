namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Leia 1 valor inteiro N, que representa o número de casos de teste que vem
            a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles 
            com uma casa decimal. Apresente a média ponderada para cada um destes 
            conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo 
            valor tem peso 3 e o terceiro valor tem peso 5.
            */

            int N = 0;
            double media1 = 0.0, media2 = 0.0, media3 = 0.0;
            string[] casos;

            Console.Write("Digite o número de casos de teste: ");
            N = int.Parse(Console.ReadLine());

            for(int i = 1; i <= N; i++){
                Console.Write($"Digite 3 valores reais(separado por espaços) para o {i}° caso: ");
                casos = Console.ReadLine().Split(' ');
                
                if(i == 1) {
                    media1 = (double.Parse(casos[0])*2 + double.Parse(casos[1])*3 + double.Parse(casos[2])*5) / 10;
                }
                if(i == 2) {
                    media2 = (double.Parse(casos[0])*2 + double.Parse(casos[1])*3 + double.Parse(casos[2])*5) / 10;
                }
                if(i == 3) {
                    media3 = (double.Parse(casos[0])*2 + double.Parse(casos[1])*3 + double.Parse(casos[2])*5) / 10;
                }
            }

            Console.WriteLine("Média ponderada:");
            Console.WriteLine($"1° Caso: {media1:F1}");
            Console.WriteLine($"2° Caso: {media2:F1}");
            Console.WriteLine($"3° Caso: {media3:F1}");
        }
    }
}
