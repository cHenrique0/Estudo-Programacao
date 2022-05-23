#nullable disable

namespace ex2_ExerciciosFixacao
{
    class Program
    {
        static void Main(string[] args)
        {
            /* Exercicio 1
            Fazer um programa para ler os valores da largura e altura de um retângulo.
            Em seguida, mostrar na tela o valor de sua área, perímetro e diagonal.
            */
            /*
            Retangulo ret = new Retangulo();
            Console.WriteLine("Digite as informações do retangulo");
            Console.Write("Largura: ");
            ret.Largura = double.Parse(Console.ReadLine());
            Console.Write("Altura: ");
            ret.Altura = double.Parse(Console.ReadLine());

            Console.WriteLine();
            Console.WriteLine(ret);
            */

            /* Exercico 2
            Fazer um programa para ler os dados de um funcionário (nome, salário bruto
            e imposto). Em seguida, mostrar os dados do funcionário (nome e salário 
            líquido). Em seguida, aumentar o salário do funcionário com base em uma 
            porcentagem dada (somente o salário bruto é afetado pela porcentagem) e 
            mostrar novamente os dados do funcionário.
            */

            /*
            Funcionario funcionario = new Funcionario();

            Console.WriteLine("Digite as informações do funcionário");
            Console.Write("Nome: ");
            funcionario.Nome = Console.ReadLine();
            Console.Write("Salário bruto: ");
            funcionario.SalarioBruto = double.Parse(Console.ReadLine());
            Console.Write("Imposto: ");
            funcionario.Imposto = double.Parse(Console.ReadLine());

            Console.WriteLine();
            Console.WriteLine($"Funcionário: {funcionario}");

            Console.WriteLine();
            Console.Write("Digite a porcentagem para aumentar o salário: ");
            double novaPorcentagem = double.Parse(Console.ReadLine());
            funcionario.AumentarSalario(novaPorcentagem);

            Console.WriteLine();
            Console.Write($"Dados atualizados: {funcionario}");
            */

            /* Exercicio 3
            Fazer um programa para ler o nome de um aluno e as três notas que ele 
            obteve nos três trimestres do ano(primeiro trimestre vale 30 e o segundo 
            e terceiro valem 35 cada). Ao final, mostrar qual a nota final do aluno 
            no ano. Dizer também se o aluno está APROVADO ou REPROVADO e, em caso 
            negativo, quantos pontos faltam para o aluno obter o mínimo para ser 
            aprovado (que é 60 pontos).
            */

            Aluno aluno = new Aluno();

            Console.Write("Digite o nome do aluno: ");
            aluno.Nome = Console.ReadLine();
            Console.WriteLine("Digite as 3 notas do aluno");
            Console.Write("Nota 1: ");
            aluno.Nota1 = double.Parse(Console.ReadLine());
            Console.Write("Nota 2: ");
            aluno.Nota2 = double.Parse(Console.ReadLine());
            Console.Write("Nota 3: ");
            aluno.Nota3 = double.Parse(Console.ReadLine());

            Console.WriteLine();
            aluno.Situacao();

            /*
            */
        }
    }
}
