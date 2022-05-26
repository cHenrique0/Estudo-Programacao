#nullable disable

namespace Praticando
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Fazer um programa para ler dois números inteiros M e N, e depois ler uma
            matriz MxN contendo números inteiros, podendo haver repetições.
            Em seguida, ler um número inteiro X que pertence à matriz. Para cada
            ocorrência de X, mostrar os valores à esquerda, acima, à direita e abaixo
            de X, quando houver.
            */

            int M, N, element;
            int[,] matrix;

            Console.WriteLine("Enter matrix order MxN");
            Console.Write("M: ");
            M = int.Parse(Console.ReadLine());
            Console.Write("N: ");
            N = int.Parse(Console.ReadLine());

            matrix = new int[M, N];
            
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                Console.Write($"Enter the elements of #{i+1} line(eg.: 1 2 3): ");
                string[] elements = Console.ReadLine().Split(' ');
                
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    matrix[i, j] = int.Parse(elements[j]);
                }
            }

            Console.WriteLine();
            Console.WriteLine("Matrix: ");
            for (int lin = 0; lin < matrix.GetLength(0); lin++)
            {
                for (int col = 0; col < matrix.GetLength(1); col++)
                {
                    Console.Write(matrix[lin, col] + " ");
                    
                    if(col == matrix.GetLength(1) - 1)
                        Console.WriteLine();
                }
            }

            Console.WriteLine();
            Console.Write("Enter an element of the matrix: ");
            element = int.Parse(Console.ReadLine());
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    if(element == matrix[i, j])
                    {
                        Console.WriteLine($"Position [{i}, {j}]");

                        if(j > 0)
                            Console.WriteLine($"Left: {matrix[i, j-1]}");
                        if(i > 0)
                            Console.WriteLine($"Up: {matrix[i-1, j]}");
                        if(j < N - 1)
                            Console.WriteLine($"Right: {matrix[i, j+1]}");
                        if(i < M - 1)
                            Console.WriteLine($"Down: {matrix[i+1, j]}");
                    }
                }
            }
        }
    }
}