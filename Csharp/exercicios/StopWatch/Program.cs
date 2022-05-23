#nullable disable

namespace StopWatch {

    class Program {

        static void Main(string[] args) {

            Loading("Starting");
            Menu();

        }

        static void Menu() {

            Console.Clear();
            Console.WriteLine("+----------------------------+");
            Console.WriteLine("|            Menu            |");
            Console.WriteLine("+----------------------------+");
            Console.WriteLine("|       [s] - Segundos       |");
            Console.WriteLine("+----------------------------+");
            Console.WriteLine("|       [m] - Minutos        |");
            Console.WriteLine("+----------------------------+");
            Console.WriteLine("|       [0] - Sair           |");
            Console.WriteLine("+----------------------------+");
            Console.WriteLine("Obs: digite a opção após o tempo desejado.");
            Console.WriteLine("ex: 10s para 10 segundos, 10m para 10 minutos");

            Console.WriteLine("Quanto tempo deseja cronometrar?");
            
            char option = ' ';
            int time = 0;
            int multiplier = 1;
            
            // Entrada do usuario
            string dataInput = Console.ReadLine().ToLower();
            
            // Separando a opção s ou m
            option = char.Parse(dataInput.Substring(dataInput.Length-1, 1));

            // Separando o tempo a ser contado
            time = int.Parse(dataInput.Substring(0, dataInput.Length-1));

            if(option == 'm') {
                multiplier = 60;
            }

            // Sair da aplicação caso o usuario digite 0
            if(time == 0) {
                Loading("Exiting");
                System.Environment.Exit(0);
            }

            PreStart(time * multiplier);

        }

        static void PreStart(int time) {
            Console.Clear();
            Console.WriteLine("Ready...");
            Thread.Sleep(1000);
            Console.WriteLine("Set...");
            Thread.Sleep(1000);
            Console.WriteLine("GO!!!");
            Thread.Sleep(1000);
            
            Start(time);
        }

        static void Loading(string name) {
            Console.Clear();
            for(int i = 0; i < 3; i++) {
                name += '.';
                Console.WriteLine(name);
                Thread.Sleep(1000);
                Console.Clear();
            }
        }

        static void Start(int time) {
            
            int currentTime = 0;

            while(currentTime != time) {

                Console.Clear();
                currentTime++;
                Console.WriteLine($"{currentTime} s");                
                Thread.Sleep(1000);
            }

            Console.Clear();
            Console.WriteLine("Finished");
            Thread.Sleep(2000);
            Menu();
        }
    }
}
