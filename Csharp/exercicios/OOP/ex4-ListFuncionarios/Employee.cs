using System.Globalization;

namespace ex4_ListFuncionarios
{
    public class Employee
    {
        public int ID { get; private set; }
        public string Name { get; private set; }
        public decimal Salary { get; private set; }

        public Employee(int id, string name, decimal salary)
        {
            ID = id;
            Name = name;
            Salary = salary;
        }

        public void IncreaseSalary(decimal percentage)
        {
            Salary += (Salary * (percentage/100));
        }

        public override string ToString()
        {
            return $"ID: {ID}\nName: {Name}\nSalary: {Salary.ToString("C", CultureInfo.CreateSpecificCulture("en-US"))}\n";
        }
    }
}