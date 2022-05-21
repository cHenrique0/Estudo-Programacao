namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Fazer um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. 
            Em seguida, calcule e mostre:
                a) a área do triângulo retângulo que tem A por base e C por altura.
                b) a área do círculo de raio C. (pi = 3.14159)
                c) a área do trapézio que tem A e B por bases e C por altura.
                d) a área do quadrado que tem lado B.
                e) a área do retângulo que tem lados A e B.
            */

            double A, B, C, areaTriangulo, areaCirculo, areaTrapezio, areaQuadrado, areaRetangulo;

            string[] valores;

            Console.WriteLine("Digite 3 valores decimais separados por espaço:");
            valores = Console.ReadLine().Split(" ");

            A = double.Parse(valores[0]);
            B = double.Parse(valores[1]);
            C = double.Parse(valores[2]);

            areaTriangulo = ( A * C ) / 2;
            areaCirculo = 3.14159 * Math.Pow(C, 2);
            areaTrapezio = ( ( A + B ) * C ) / 2;
            areaQuadrado = Math.Pow(B, 2);
            areaRetangulo = A * B;

            Console.WriteLine($"Triângulo = {areaTriangulo:F2}");
            Console.WriteLine($"Círculo = {areaCirculo:F2}");
            Console.WriteLine($"Trapézio  = {areaTrapezio:F2}");
            Console.WriteLine($"Quadrado  = {areaQuadrado:F2}");
            Console.WriteLine($"Retângulo = {areaRetangulo:F2}");

        }
    }
}
