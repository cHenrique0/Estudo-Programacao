# TimeSpan
Representa uma duração.  
É um tipo valor(`struct`)  
  
Um objeto `TimeSpan` internamente armazena uma duração na forma de _tick_(100 nanosegundos).  

Exemplos:
```c#
TimeSpan t1 = new TimeSpan(0, 1, 30); // hora, minuto, segundo
Console.WriteLine(t1); // 00:01:30
```

## 1. Construtores:
```c#
TimeSpan t1 = new TimeSpan(); // nenhum argumento
TimeSpan t2 = new TimeSpan(900000000L); // ticks como argumento
TimeSpan t3 = new TimeSpan(2, 10, 31); // horas, minutos, segundos
TimeSpan t4 = new TimeSpan(1, 2, 10, 31); // dias, horas, minutos, segundos
TimeSpan t5 = new TimeSpan(1, 2, 10, 31, 321); // dias, horas, minutos, segundos, milisegundos

Console.WriteLine(t1); // 00:00:00
Console.WriteLine(t2); // 00:01:30 (esse tempo depende da quantidade de ticks)
Console.WriteLine(t3); // 02:10:31
Console.WriteLine(t4); // 1.02:10:31
Console.WriteLine(t5); // 1.02:10:31.3210000
```

## 2. `TimeSpan.From`
```c#
TimeSpan t1 = TimeSpan.FromDays(1.5); // 1 dia e meio
TimeSpan t2 = TimeSpan.FromHours(1.5); // 1 hora e meia
TimeSpan t3 = TimeSpan.FromMinutes(1.5); // 1 minuto e meio
TimeSpan t4 = TimeSpan.FromSeconds(1.5); // 1 segundo e meio
TimeSpan t5 = TimeSpan.FromMilliseconds(1.5); // 1 milisegundo e meio
TimeSpan t6 = TimeSpan.FromTicks(900000000L); // ticks (só aceita longs)

Console.WriteLine(t1); // 1.12:00:00
Console.WriteLine(t2); // 01:30:00
Console.WriteLine(t3); // 00:01:30
Console.WriteLine(t4); // 00:00:01.5000000
Console.WriteLine(t5); // 00:00:00.0015000
Console.WriteLine(t6); // 00:01:30
```
## 3. Algumas propriedades
```c#
TimeSpan max = TimeSpan.MaxValue;
TimeSpan min = TimeSpan.MinValue;
TimeSpan zero = TimeSpan.Zero;

Console.WriteLine(max);  // 10675199.02:48:05.4775807
Console.WriteLine(min);  // -10675199.02:48:05.4775808
Console.WriteLine(zero); // 00:00:00

TimeSpan ts = new TimeSpan(2, 3, 5, 7, 11);
Console.WriteLine(ts); // 2.03:05:07.0110000
Console.WriteLine($"Dias: {ts.Days}"); // 2
Console.WriteLine($"Horas: {ts.Hours}"); // 3
Console.WriteLine($"Minutos: {ts.Minutes}"); // 5
Console.WriteLine($"Segundos: {ts.Seconds}"); // 7
Console.WriteLine($"Milisegundos: {ts.Milliseconds}"); // 11
Console.WriteLine($"Ticks: {ts.Ticks}"); // 1839070110000
Console.WriteLine($"Total de dias: {ts.TotalDays}"); // 2.1285533680555555
Console.WriteLine($"Total de horas: {ts.TotalHours}"); // 51.085280833333336
Console.WriteLine($"Total de minutos: {ts.TotalMinutes}"); // 3065.11685
Console.WriteLine($"Total de segundos: {ts.TotalSeconds}"); // 183907.011
Console.WriteLine($"Total de milisegundos: {ts.TotalMilliseconds}"); // 183907011
```

## 4. Operações com `TimeSpan`
```c#
TimeSpan t1 = new TimeSpan(1, 30, 10);
TimeSpan t2 = new TimeSpan(0, 10, 5);

TimeSpan sum = t1.Add(t2);
TimeSpan sub = t1.Subtract(t2);
TimeSpan mult = t2.Multiply(2.0);
TimeSpan div = t2.Divide(2.0);

Console.WriteLine(sum);   // 01:40:15
Console.WriteLine(sub);   // 01:20:05
Console.WriteLine(mult);  // 00:20:10
Console.WriteLine(div);   // 00:05:02.5000000
```
