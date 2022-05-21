namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Escreva um programa para ler as coordenadas (X,Y) de uma quantidade
            indeterminada de pontos no sistema cartesiano. Para cada ponto escreva 
            o quadrante a que ele pertence. O algoritmo será encerrado quando pelo 
            menos uma de duas coordenadas for NULA (nesta situação sem escrever 
            mensagem alguma).
            */
            
            int x, y;

            Console.Write("Digite dois números inteiros(separados por espaço): ");
            string[] numeros = Console.ReadLine().Split(" ");

            x = int.Parse(numeros[0]);
            y = int.Parse(numeros[1]);

            while(x != 0 && y != 0) {
                if( x > 0 && y > 0 )
                    Console.WriteLine("1° Quadrante");
                else if( x < 0 && y > 0 )
                    Console.WriteLine("2° Quadrante");
                else if( x < 0 && y < 0 )
                    Console.WriteLine("3° Quadrante");
                else if( x > 0 && y < 0 )
                    Console.WriteLine("4° Quadrante");
                Console.Write("Digite dois números inteiros(separados por espaço): ");
                numeros = Console.ReadLine().Split(" ");

                x = int.Parse(numeros[0]);
                y = int.Parse(numeros[1]);
            }

        }
    }
}
