# Flexbox

Projetado como um modelo de layout unidimensional e como um método que pode ofercer distribuição de espaço entre itens em uma interface e recursos de alinhamento.  

## 1. Flex Container
É a **tag** que envolve os itens. Nessa tag será aplicada a _propriedade_ `display: flex`. Ela transforma todos os seus itens _filhos_ em **flex itens**.  
Essa propriedade pode ser aplicada a qualquer tag html.  
  
Propriedades:
- `display`: Inicializador do container.
- `flex-direction`: Direcionamento dos itens. É a propriedade que estabelece o eixo principal do container.
  - `row`: à direção do texto. Esquerda para direita. É o padrão.
  - `row-reverse`: sentido oposto ao row.
  - `column`: ordenação de cima para baixo, em coluna unica.
  - `column-reverse`: ordenação inversa à column.
- `flex-wrap`: Define se haverá ou não a quebra de linha. Por padrão não há quebra de linha. Assim os flex itens são compactado além do limite do container.
  - `nowrap`: é o padrão. Não permite a quebra de linha.
  - `wrap`: permite a quebra de linha assim que um dos flex itens não puder mais ser compactado dentrod o container.
  - `wrap reverse`: a quebra de linha funciona de forma inversa, ou seja, a nova linha é adicionada acima da linha atual.
- `flex-flow`: Abreviação para `flex-direction` e `flex-wrap`.
- `justify-content`: Alinha os itens do container de acordo com a sua direção.
- `align-items`: Alinha os itens de acordo com o eixo do container.
- `align-content`: Alinha as linhas do container.

## 2. Flex Item
São os elementos filhos diretos do Flex Container. E também podem se tornar Flex Container.  
  
Propriedades:
- `flex-grow`: Define o fator de crescimento.
- `flex-basis`: Define o tamanho inicial do item.
- `flex-shrink`: Define a capacidade de recursão.
- `flex`: Abreviação para as 3 propriedades acima.
- `order`: Ordem de distribuição e listagem dos itens.
- `align-self`: Define o alinhamento de um item especifico do container.