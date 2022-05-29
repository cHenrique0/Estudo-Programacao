# DateTime

É um tipo especifico de dados para tratar datas
É implementado usando struct

---
## Trabalhando com Datas

### 1. Criando uma data
```c#
DateTime date = new DateTime();
Console.WriteLine(date); // mostra 01/01/0001 00:00:00 que é a data padrão
```
### 2. Criando uma data especificando os valores
Para criar um DateTime especifico precisamos passar os valores desejados por parametro.
Os parametros seguem a seguinte ordem: ano, mês, dia, horas, minutos, segundos.
```c#
DateTime date = new DateTime(2010, 8, 25, 8, 23, 15);
Console.WriteLine(date); // mostra 08/25/2010 08:23:15
```
### 3. Acessando os valores de forma individual
```c#
DateTime date = new DateTime(2010, 8, 25, 8, 23, 15);
DateTime date = new DateTime(2010, 8, 25, 8, 23, 15);
Console.WriteLine(date);            // 08/25/2010 08:23:15
Console.WriteLine(date.Day);        // 25
Console.WriteLine(date.Month);      // 8
Console.WriteLine(date.Year);       // 2010
Console.WriteLine(date.Hour);       // 8
Console.WriteLine(date.Minute);     // 23
Console.WriteLine(date.Second);     // 15
Console.WriteLine(date.DayOfWeek);  // Wednesday -> quarta-feira
Console.WriteLine(date.DayOfYear);  // 237
```
### 4. Data e hora atuais
```c#
DateTime date1 = DateTime.Now;  // data e hora atuais
Console.WriteLine(date1);

DateTime date2 = DateTime.Today; // apenas a data atua, e horas zeradas
Console.WriteLine(date2);
```

### 5. `DateTime.Parse`
```c#
DateTime d1 = DateTime.Parse("2000-08-15");
DateTime d2 = DateTime.Parse("2000-08-15 13:08:56");

Console.WriteLine(d1);
Console.WriteLine(d2);
```

### 6. `DateTime.ParseExact`
```c#
DateTime d1 = DateTime.ParseExact("2000-08-15", "yyyy-MM-dd", CultureInfo.InvariantCulture);
DateTime d2 = DateTime.ParseExact("15/08/2000", "dd/MM/yyyy", CultureInfo.InvariantCulture);

Console.WriteLine(d1);
Console.WriteLine(d2);
```

---
## Formatando Datas

Usando `String.Format` podemos formatas uma data.
Algumas opções:
- yyyy: ano
- MM: mês
- dd: dia
- hh: hora
- mm: minutos
- ss: segundos
- ff: frações de segundo
- z: timezone(fuso)
```c#
DateTime date = DateTime.Now;
Console.WriteLine("{0:yyyy}", date);
Console.WriteLine("{0:MM}", date);
Console.WriteLine("{0:dd}", date);
Console.WriteLine("{0:dd/MM/yyyy - hh:mm:ss}", date);
```
Outras formatações
```c#
DateTime date = DateTime.Now;
Console.WriteLine("{0:t}", date);   // 22:08
Console.WriteLine("{0:T}", date);   // 22:08:01
Console.WriteLine("{0:d}", date);   // 05/19/2022
Console.WriteLine("{0:D}", date);   // Thursday, 19 May 2022
Console.WriteLine("{0:f}", date);   // Thursday, 19 May 2022 22:08
Console.WriteLine("{0:g}", date);   // 05/19/2022 22:08
Console.WriteLine("{0:y}", date);   // 2022 May
Console.WriteLine("{0:r}", date);   // Thu, 19 May 2022 22:08:01 GMT
Console.WriteLine("{0:s}", date);   // 2022-05-19T22:11:26
Console.WriteLine("{0:u}", date);   // 2022-05-19 22:12:05Z
```
---
## Adicionando valores
```c#
DateTime date = DateTime.Now;
Console.WriteLine(date);
// Incrementa dias na data, mudando o mês e o ano automaticamente, caso necessário
Console.WriteLine(date.AddDays(10));
Console.WriteLine(date.AddMonths(2));
// Podemos passar numeros negativos como parametro
Console.WriteLine(date.AddYears(-2));
```

## Diferença entre datas
```c#
DateTime inicio = new DateTime(2000, 10, 15);
DateTime fim = new DateTime(2000, 10, 18);

TimeSpan diferenca = fim.Subtract(inicio);

Console.WriteLine(diferenca);  // 3.00:00:00 - diferença de 3 dias
```
---

