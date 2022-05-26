#nullable disable

namespace Praticando
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Fazer um programa para ler um número inteiro N e uma matriz de ordem N
            contendo números inteiros. Em seguida, mostrar a diagonal principal e a
            quantidade de valores negativos da matriz.
            */

            int N, negativeAmount = 0;
            int[,] matrix;

            Console.Write("Enter matrix order: ");
            N = int.Parse(Console.ReadLine());

            matrix = new int[N, N];
            
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                Console.Write($"Enter the elements of #{i+1} line(eg.: 1 2 3): ");
                string[] elements = Console.ReadLine().Split(' ');
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    matrix[i, j] = int.Parse(elements[j]);
                    if(matrix[i, j] < 0)
                        negativeAmount++;
                }
            }

            Console.WriteLine();
            Console.WriteLine("Matrix: ");
            for (int lin = 0; lin < matrix.GetLength(0); lin++)
            {
                for (int col = 0; col < matrix.GetLength(1); col++)
                {
                    Console.Write(matrix[lin, col] + " ");
                    if(col == 2)
                        Console.WriteLine();
                }
            }

            Console.WriteLine();
            Console.Write("Main diagonal: ");
            for (int lin = 0; lin < matrix.GetLength(0); lin++)
            {
                for (int col = 0; col < matrix.GetLength(1); col++)
                {
                    if(lin == col)
                        Console.Write(matrix[lin, col] + " ");
                }
            }

            Console.WriteLine();
            Console.WriteLine($"Negative numbers: {negativeAmount}");
        }
    }
}