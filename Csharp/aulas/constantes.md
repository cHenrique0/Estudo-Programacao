## Constantes

- É possivel armazenar informações em constantes;
- As constantes **NÃO PODEM** ser alteradas;
- Uma vez criada, somos obrigados a atribuir um valor;
    - Feito isto, a constante não poderá ser modificada novamente;
- Não funcionam com a utilização do <code>var</code>
- São mais otimizadas que as variáveis;
- Recomendadas para usos frequentes;

- A definição de constante é dada pela palavra reservada const antes do tipo da variável;
- Caso não seja informado um valor, o valor padrão será atribuido;

```csharp
const int IDADE_MINIMA;         // Correto, inicia com ZERO
const int IDADE_MINIMA = 10;    // Correto, inicia com 10
const var IDADE_MINIMA = 10;    // ERRADO!
const var IDADE_MINIMA;         // ERRADO!
```

- É comum os nomes das constantes serem escritos com todas as letras maiúsculas e as palavras separadas por <code>_</code>
    - A ideia é que ao olhar o código, o desenvolvedor saiba que aquilo é uma constante;