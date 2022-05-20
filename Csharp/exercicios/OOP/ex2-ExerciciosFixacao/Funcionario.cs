
namespace ex2_ExerciciosFixacao
{
    public class Funcionario
    {
        public string Nome = "";
        public double SalarioBruto = 0.0;
        public double Imposto = 0.0;

        public double SalarioLiquido() {
            return SalarioBruto - Imposto;
        }

        public void AumentarSalario(double porcentagem) {
            SalarioBruto += (SalarioBruto * (porcentagem/100.0));
        }

        public override string ToString()
        {
            return $"{Nome}, R$ {SalarioLiquido()}";
        }
    }
}