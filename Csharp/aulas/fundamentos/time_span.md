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