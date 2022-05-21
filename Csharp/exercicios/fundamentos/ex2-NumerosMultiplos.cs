namespace Praticando {

    class Program {

        static void Main(string[] args) {

            /*
            Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem
            "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são 
            múltiplos entre si.

            Atenção: os números devem poder ser digitados em ordem crescente ou decrescente.
            */

            string[] numeros;
            int num_1, num_2;

            Console.Write("Digite 2 números inteiros (separados por espaço): ");
            numeros = Console.ReadLine().Split(" ");
            num_1 = int.Parse(numeros[0]);
            num_2 = int.Parse(numeros[1]);

            if (num_1 < num_2) {
                if(num_2 % num_1 == 0){
                    Console.WriteLine("São multiplos");
                }
                else{
                    Console.WriteLine("Não são multiplos");
                }
            }
            else {
                if(num_1 % num_2 == 0){
                    Console.WriteLine("São multiplos");
                }
                else{
                    Console.WriteLine("Não são multiplos");
                }
            }
        }
    }
}
