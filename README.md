# Projeto de Algoritmos de Ordenação

## Objetivo
Nesta atividade, cada grupo será responsável por implementar um dos algoritmos de ordenação em Python e seguir o fluxo de trabalho colaborativo utilizando Git e GitHub. O objetivo principal é estimular a lógica de programação, a colaboração entre equipes e o uso adequado de ferramentas de versionamento de código.

## Regras Gerais
1. **Divisão de Grupos**: 
   - Cada grupo deverá criar uma branch para resolver o algoritmo abaixo:
     - **Bubble Sort**
   
2. **Implementação**:
   - Cada grupo deve implementar o algoritmo atribuído em Python.
   - **Não é permitido o uso de métodos embutidos das listas** como `sort()`, `insert()`, `append()` ou qualquer outro método que realize a ordenação ou manipulação direta das listas.
   - O foco é na lógica, então todos os passos devem ser explicitamente implementados.
   - **É proibido o uso de Inteligência Artificial** (IA) para gerar ou ajudar na solução do código.
   - **É proibido consultar o algoritmo pronto na internet** ou copiar código de fontes externas. O objetivo é que vocês desenvolvam suas próprias soluções.
   - Consulte a seção **Comandos Permitidos** para saber o que pode ser utilizado.
   - Para cada iteração, print a lista para que seja possível acompanhar a ordenação.

3. **Fluxo de Trabalho Git/GitHub**:
   - Cada grupo deve clonar o repositório do projeto:  
     ```
     git clone https://github.com/ProfDudarts/ordenacao
     ```
   - Crie uma nova branch com o prefixo `grupo_[00])_` e o nome do algoritmo que estão implementando. Exemplo para Bubble Sort:
     ```
     git checkout -b grupo_00_bubble_sort
     ```
   - Após implementar o algoritmo, faça o commit das alterações, ou das correções, quando houver:
     ```
     git add .
     git commit -m "Implementação do Bubble Sort"
     ```
   - Faça o push da sua branch para o repositório remoto:
     ```
     git push origin bubble_sort
     ```
   - Abra um **Pull Request** (PR) no GitHub para que o código seja revisado por outra equipe.
   
4. **Revisão de Código**:
   - Uma equipe diferente da que implementou o código será responsável por revisar o **Pull Request**.
   - A equipe revisora deve verificar se:
     - O algoritmo foi implementado corretamente.
     - O código segue as regras estabelecidas (não usar métodos proibidos, por exemplo).
     - Não há bugs aparentes ou problemas de lógica.
   - Caso a revisão seja aprovada, a equipe revisora deve fazer o **merge** do código para a branch principal.
   - Se houver problemas, a equipe revisora deve solicitar ajustes e feedback ao grupo responsável pela implementação.

5. **Comandos Permitidos**:
   - **Controle de fluxo**: `if`, `for`, `while`, `else`, `elif`,
   - **Manipulação básica de listas**: Acessar elementos diretamente (`arr[i]`), trocar valores entre elementos, etc.
   - **Operadores do Python e os comandos**: `range`, `print`, `len`
   - **Funções definidas pelo usuário**: `def`
   - **Manipulação de variáveis** e uso de listas auxiliares quando permitido.

6. **Algoritmos e Regras Específicas**:
   - Cada grupo deve implementar o algoritmo conforme descrito abaixo:
   
   ### Bubble Sort
   - Implementar o algoritmo que ordena elementos através de trocas consecutivas de elementos adjacentes.
   - A ordenação deve ser feita diretamente na lista.
   - Link de Referência: [Bublle Sort](https://www.youtube.com/watch?v=i2IKFmI_gyk)

## Instruções para Revisão de Pull Request
- Após o Pull Request ser aberto por um grupo, outro grupo será designado para revisar o código.
- O grupo revisor deve:
  1. Verificar se o código cumpre todas as regras e implementa o algoritmo corretamente.
  2. Comentar no Pull Request sugerindo melhorias, se necessário.
  3. Aprovar ou solicitar mudanças.

## Instruções Finais
1. Após a aprovação e merge do Pull Request, todos os grupos devem garantir que o código final esteja funcionando corretamente.
2. **O uso de IA ou consultas a algoritmos prontos da internet é estritamente proibido**. O código deve ser resultado do esforço e compreensão de cada equipe.
3. O prazo final para submissão e revisão dos Pull Requests será informado em sala de aula.
4. O objetivo desta atividade é desenvolver suas habilidades em:
   - Lógica de programação.
   - Colaboração em equipe.
   - Uso de Git e GitHub para trabalho colaborativo.
5. A primeira implementação correta será mergeada com a branch main.

Bom trabalho!
