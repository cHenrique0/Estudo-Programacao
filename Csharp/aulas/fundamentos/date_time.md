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
DateTime date = DateTime.Now;
Console.WriteLine(date);
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
