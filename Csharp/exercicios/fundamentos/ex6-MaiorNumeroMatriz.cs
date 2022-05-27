#nullable disable

namespace Praticando
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Leia uma matriz 10 x 10 e escreva a localização (linha e a coluna) 
            do maior valor.
            */

            int[,] matrix = new int[3, 3];
            int max;

            Console.WriteLine("Enter the elements of the matrix");
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                Console.Write($"Enter the #{i+1} elements(eg.: 1 2 3): ");
                string[] line = Console.ReadLine().Split(' ');
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    matrix[i, j] = int.Parse(line[j]);
                }
            }

            max = matrix[0, 0];

            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    if(matrix[i, j] > max)
                        max = matrix[i, j];
                }
            }

            Console.WriteLine($"Max: {max}");
        }
    }
}
