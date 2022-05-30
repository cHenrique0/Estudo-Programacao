# Orientação à objetos
  
É um modelo de análise, projeto e programação de software baseado na composição e interação entre diversas unidades chamadas de "**objetos**".  
O básico que um objeto possui é:
- A capacidade de interagir com outros objetos
- Realizar ações(métodos)
- Estado intero(dados)
  
Os objetos pode ser ferramentas de programação de baixo nível, como listas, pilhas, árvores, semelhante aos tipos de dados abstratos tradicionais.  
Eles tembém podem ser abstrações de nível mais alto que refletem o que um programa pretende modelar: um caixa eletrônico, uma coleção de objetos gráficos em uma tela, etc.  
  
## 1. Objetos
É a unidade utilizada para modelar objetos do mundo real.  
Possuem estado(variáveis de instância), métodos(definições que estabelecem como responder certas mensagens que recebem externamente).
- Estado: implementado através de um conjunto de atributos
- Comportamento: define como um objeto reage às ações de outros objetos
- Identidade única: propriedade que distingue um objeto de outros objetos

## 2. Encapsulamento
É definido como uma técnica para minimizar as interdependências entre "_módulos_".
Beneficios:
- Segurança: protege os atributos dos objetos de serem corrompidos por outros objetos
- Independência: "_esconde_" seus atributos e métodos
  
## 3. Classes
É uma família de objetos com componentes variáveis e métodos semelhantes. As classes são como fábricas de objetos.  

### 3.1 Classes x Objetos
A mesma diferença entre o conceito de um cachorro(universal) e um cachorro em particular.  
Uma classe descreve como os cachorros são:
- Atributos: peso, altura, cor dos olhos, cor do pelo, etc.
- Ações: comer, dormir, latir, correr, andar, etc.

Um cachorro particular possui:
- Peso: 30kg
- Altura: 56cm
- Cor dos olhos: pretos
- Cor do pelo: amarelo
- etc.

Em outros termos, o objeto é a **instância** de uma classe.  

### 3.2 Variáveis de instância
Um objeto utiliza variáveis de instância para armazenar seu estado. O estado de um objeto é o conjunto de valores que determinam como um objeto reage às chamadas de métodos.
Exemplo em C#:
```c#
Greeter greeter1 = new Greeter();
Greeter greeter2 = new Greeter();
// greeter1 e greeter2 são variáveis de instância
```

## 4. Herança
A classificação de objetos é uma característica fundamental das linaguagens orientadas à objetos. Uma classe é uma família de objetos com componentes e métodos variáveis semelhantes. Uma subclasse estende uma classe com componentes adicionais e/ou métodos adicionais(ou substituindo-os). Casa subclasse pode ter susas próprias subclasses, então podemos construir uma hierarquia de classes.  
A **herança** também é característica de linguagens orientadas à objetos. Uma sublcasse(filha) _herda_(compartilha) todos os métodos de sua superclass(pai), a menos que a subclasse substituia explicitamente qualquer um desses métodos. De fato, toda hierarquia de classes pode herdar métodos de uma classe ancestral. A herança tem um grande impacto na produtividade do programador.  

### 4.1 Porque usar Herança?
A reusabilidade é uma qualidade desejável no desenvolvimente de grandes sistemas.  
Tipos abstratos de dados(TAD), com seus encapsulamente e controle de acesso, são as unidades de reuso nas linguagens orientadas à objetos.  
TAD's em linguagens OO são chamadas de classes, e suas instâncias são objetos.   
- Problema 1: as capacidades de um tipo existente podem não atender plenamente  as necessidades da aplicação cliente, requerendo adaptações.  Porém, isso iria requerer o acesso e a compreensão do código existente dentro do tipo.
- Problema 2: Muitas modelagens tratam de categorias de objetos que são relacionados de modo hierárquico, como relações de pais e filhos.

### 4.2 Sobrescrevendo métodos da superclasse