
namespace ex3_ContaBancaria
{
    public class Conta
    {
        private const double TAXA_SAQUE = 5.00;

        public int Numero { get; private set; }
        public string Titular { get; set; }
        public double Saldo { get; private set; }

        public Conta(int numeroConta, string nomeTitular)
        {
            Numero = numeroConta;
            Titular = nomeTitular;
        }

        public Conta(int numeroConta, string nomeTitular, double depositoInicial) : this(numeroConta, nomeTitular)
        {
            this.Deposito(depositoInicial);
        }
        
        public void Deposito(double valor)
        {
            if(valor > 0)
            {
                Saldo += valor;
                Console.WriteLine("Depósito efetuado com sucesso");
                return;
            }
            Console.WriteLine("O valor do deposito deve ser no minimo R$ 0,01");
        }

        public void Saque(double valor)
        {
            if(valor > 0)
            {
                Saldo = (Saldo - TAXA_SAQUE) - valor;
                Console.WriteLine("Saque efetuado com sucesso");
                return;
            }
            Console.WriteLine("O valor do deposito deve ser no minimo R$ 0,01");
        }

        public override string ToString()
        {
            return $"\nDados da conta\nNúmero: {Numero}\nTitular: {Titular}\nSaldo: R$ {Saldo:F2}";
        }
    }
}