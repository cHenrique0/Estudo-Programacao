#nullable disable

namespace ex4_ListFuncionarios
{
    class Program
    {
        static void Main(string[] args)
        {
            // See instructions in the README.md file in this folder

            List<Employee> employees = new List<Employee>();
            int numberOfEmployee, employeeID, increaseSalaryID;
            string employeeName;
            decimal employeeSalary, increaseSalaryPercentage;

            Console.Write("How many employees will be registered? ");
            numberOfEmployee = int.Parse(Console.ReadLine());
            
            Console.WriteLine();
            Console.WriteLine("Enter the employee information");
            for (int i = 1; i <= numberOfEmployee; i++)
            {
                Console.WriteLine($"Employee #{i}");
                Console.Write("ID: ");
                employeeID = int.Parse(Console.ReadLine());
                // Check if employee ID already exists. If true, a different ID must be entered
                while(employees.Any(x => x.ID == employeeID))
                {
                    Console.WriteLine("This ID already exists. Choosen another.");
                    Console.Write("ID: ");
                    employeeID = int.Parse(Console.ReadLine());
                }
                Console.Write("Name: ");
                employeeName = Console.ReadLine();
                Console.Write("Salary: ");
                employeeSalary = decimal.Parse(Console.ReadLine());
                Console.WriteLine();

                // adding the employee to the list of employees
                employees.Add(new Employee(employeeID, employeeName, employeeSalary));
            }


            Console.Write("Enter the employee ID that will have salary increase: ");
            increaseSalaryID = int.Parse(Console.ReadLine());
            // Cheking if the employee ID exists in the list of employees
            if(employees.Any(x => x.ID == increaseSalaryID))
            {
                Console.Write("Enter the percentage: ");
                increaseSalaryPercentage = decimal.Parse(Console.ReadLine());
                // Find the employee that matches the ID and increase their salary
                employees.Find(x => x.ID == increaseSalaryID).IncreaseSalary(increaseSalaryPercentage);
            }
            else
            {
                Console.WriteLine("Invalid ID! This ID doesn't exist.");
            }

            Console.WriteLine();
            Console.WriteLine("List of employees:");
            foreach (var employee in employees)
            {
                Console.WriteLine(employee);
            }
            
        }
    }
}