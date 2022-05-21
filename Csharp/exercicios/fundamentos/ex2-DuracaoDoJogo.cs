namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Leia a hora inicial e a hora final de um jogo. 
            A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em 
            um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima 
            de 24 horas.
            */

            int inicio, fim, duracao;

            Console.Write("Digite a hora de inicio e fim do jogo (separadas por espaço): ");
            string[] horas = Console.ReadLine().Split(" ");

            inicio = int.Parse(horas[0]);
            fim = int.Parse(horas[1]);

            if (inicio < fim) {
                duracao = fim - inicio;
            }
            else {
                duracao = 24 - inicio + fim;
            }
            Console.WriteLine($"O jogo durou {duracao} horas(s)");
        }
    }
}
