using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ex2_ExerciciosFixacao
{
    public class Retangulo
    {
        public double Largura = 0.0;
        public double Altura = 0.0;

        public double Area() {
            return Largura * Altura;
        }

        public double Perimetro() {
            return 2 * (Largura + Altura);
        }

        public double Diagonal() {
            return Math.Sqrt(Math.Pow(Largura, 2) * Math.Pow(Altura, 2));
        }

        public override string ToString()
        {
            return $"Área: {Area():F2}\nPerímetro: {Perimetro():F2}\nDiagonal: {Diagonal():F2}";
        }
    }
}