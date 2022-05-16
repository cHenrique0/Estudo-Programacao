namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Leia 2 valores x e y, com uma casa decimal, que devem representar as 
            coordenadas de um ponto em um plano. A seguir, determine qual o quadrante
            o ponto pertence, ou se está sobre um dos eixos cartesianos ou na origem 
            (x = y = 0).
            Se o ponto estiver na origem, escreva a mensagem “Origem”.
            Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, 
            conforme for a situação.
            */

            double x, y;

            Console.Write("Digite dois números com uma casa decimal(separados por espaço): ");
            string[] numeros = Console.ReadLine().Split(" ");

            x = double.Parse(numeros[0]);
            y = double.Parse(numeros[1]);

            if( x == 0 && y == 0 )
                Console.WriteLine("Origem");
            else if( x == 0 )
                Console.WriteLine("Eixo y");
            else if( y == 0 )
                Console.WriteLine("Eixo x");
            else if( x > 0 && y > 0 )
                Console.WriteLine("Q1");
            else if( x < 0 && y > 0 )
                Console.WriteLine("Q2");
            else if( x < 0 && y < 0 )
                Console.WriteLine("Q3");
            else if( x > 0 && y < 0 )
                Console.WriteLine("Q4");
        }
    }
}
