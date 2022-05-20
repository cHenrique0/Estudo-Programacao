using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ex2_ExerciciosFixacao
{
    public class Aluno
    {
        public string Nome = "";
        public double Nota1 = 0.0;
        public double Nota2 = 0.0;
        public double Nota3 = 0.0;

        public void Situacao() {
            double notaFinal = Nota1 + Nota2 + Nota3;
            
            if(notaFinal < 60){
                Console.WriteLine($"Nota final: {notaFinal:F2}");
                Console.WriteLine("REPROVADO");
                Console.WriteLine($"Faltaram {60 - notaFinal:F2} pontos");
                return;
            }

            Console.WriteLine($"Nota final: {notaFinal:F2}");
            Console.WriteLine("APROVADO");
        }
    }
}