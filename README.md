# traveller_algorithm
Algorithm implementation only for graphs studies

# ======================================================================
# DOCUMENTAÇÃO
# ======================================================================

# Execução

  1 - Requisitos

    python3
    pip

    Os requisitos mínimos para execução do programa são o "INTERPRETADOR PYTHON" e o instalador de pacotes "PIP" instalados na máquina. Recomendasse que a linguagem esteja na versão 3.13.1 e o instalador de pacotes na versão 24.3.1, uma vez que estas foram utilizadas durante o desenvolvimento.

  2 - Preparando o ambiente do projeto

    2.1 - Mova os arquivos do projeto para um diretório em que haja permissão para execução de arquivos .py.

    2.2 - (Opcional, mas recomendado) Crie um ambiente virtual da linguagem python através do comando "python -m venv venv" e o ative. Em sistemas Linux, isso pode ser feito através do comando "source venv/bin/activate". Em ambientes Windows, deve-se executar o arquivo em "venv\Scripts\activate" pelo cmd ou "venv\Scripts\Activate.ps1" pelo powershell.

    (ATENÇÃO: o módulo venv está incluído na linguagem a partir das versão 3.3. Se estiver usando versões mais antigas, instale globalmente o pacote virtualenv com "pip install virtualenv" e criá-lo com "virtualenv venv")

    2.3 - Instale as dependências do projeto com o comando "pip install -r requirements.txt". Isso deve ser feito no mesmo diretório de requirements.txt

  3 - Executando

    3.1 - Uma vez configurado o ambiente, basta executar o arquivo main.py com "python3 main.py".

    3.2 - No arquivo main.py é possível observar as seguintes variáveis globais

      FILENAME = "fri26_d.txt"
      ITERATIONS: int = 100
      ANT_NUMBER: int = 5
      DECAY_RATE: float = 0.5
      SHOW_EACH_ITERATION_TIME: bool = False
      PHEROMONE_INFLUENCE: float = 0.6
      VISIBILITY_INFLUENCE: float = 5

    Elas representam as variáveis que influenciam na execução do algoritmo de ACO. Antes de cada execução é possível alterá-las, salvar o arquivo e executá-lo. É importante lembrar apenas de seguir a tipagem que cada uma delas anota em sua frente (str, int, float bool). 

    Para alterar o arquivo, basta movê-lo para a pasta assets. Após isso, modifique a variável FILENAME, colocando o nome do arquivo desejado em seu lugar.

    ATENÇÃO: O arquivo DEVE ser depositado em assets, caso contrário não será possível executar o código

# Implementação

  Esse projeto foi construído utilizando o paradigma da Orientação a Objetos. A escolha por esse paradigma foi feita devido à facilidade de representação dos elementos constituintes do problema (Formiga, Colônia, Grafo) como objetos, o que permitiu um fluxo mais claro de desenvolvimento e aplicação da heurística em código.

  Como um programa escrito em OO, ele possui uma série de entidades que serão amplamente usadas. Seguem abaixo as classes criadas com uma descrição do comportamento de suas funções.

  ""Matrix"" - npmatrix.py
  
    Matrix não é uma classe que apresenta muitas funções particularmente relevantes. Foi criada como uma forma rústica de se representar um tipo, prática comum no trabalho com linguagens como TypeScript. Seu propósito é fornecer uma interface de uso similar à de uma matrix comum (matrix[i][j] retorna o valor na linha i e coluna j), porém utilizando, internamente as matrizes da biblioteca numpy, que permitem o operações vetorizadas, mais performáticas quando lidando com grandes matrizes.

    Para atingir tal objetivo os métodos especiais __repr__,  __getitem__, __setitem__, __imul__, __add__, __iadd__ foram sobrescritos na classe. Além disso, foram criados dois métodos de classse.

    @classmethod
    def initialize(cls, lines: int = 0, columns: int = 0, fill: float = 0):

      Recebe um número de linhas, colunas e um valor fill, retornando uma matriz com "lines" linhas, "columns" colunas e preenchendo todos os seus items com o valor "fill". 
    
    @classmethod
    def fromFile(cls, filePath: str) -> 'Matrix':

      Recebe um diretório no formato de uma string e retorna um objeto da classe Matrix criado a partir de uma matriz de distâncias contida no diretório.

  ""Graph"" - graph.py

    Graph é usado como camada de abstração adicional para representação do grafo do problema. Ele possui duas propriedades: matrix (a matriz de distâncias que representa o problema) e scoreMatrix (a matriz que representa o feromônio presente em cada aresta). Apenas um de seus métodos é usado:
    
    def generateScoreMatrix(self, matrix: Matrix) -> Matrix:

      Recebe uma matriz de distâncias e, através da mesma, decide o estado inicial da matriz de feromônio do problema. Após calcular o valor de feromônio das arestas, retorna uma matriz sob essas condições. O feromônio depositado em cada aresta é igual a 1 / (número de vértices) * (maior custo da matriz)

  ""Ant"" - ant.py

    Ant representa uma formiga. Pra o projeto, foi decidido que cada formiga seria responsável pelos próprios comportamentos de decisão nos percursos, bem como registro dos melhores ciclos encontrados por elas. Elas armazenam, além de sua cidade de início, o último caminho feito, caminho atual e suas respectivas distâncias. Abaixo, suas funções:

    def calcTravelProbability(self, cityA: int, cityB: int, graph: Graph, feromoneInfluence: float, visibilityInfluence: float):

      Recebe uma cidade A, uma cidade B, um grafo, um valor de influência do feromônio e um valor de influência da visibilidade. O método, através dos parâmetros dados, retorna uma probabilidade (variando de 0 a 1), da formiga se deslocar da cidade A até a cidade B.
    
    def pickNextCity(self, graph: Graph, currentCity: int) -> int:

      Recebe um grafo e a cidade atual. Através da função calcTravelProbability, o método atribui as probabilidades às cidades possíveis e escolhe entre elas aleatoriamente, dando favorecimento proporcional às probabilidades associadas a cada cidade - Isso garante relevância para os fatores feromônio e visibilidade, porém não retira totalmente a aleatoriadade do algoritmo.

      Só serão consideradas, cidades ainda não visitadas. Caso todas as cidades tenham sido visitadas, retorna -1

    def travel(self, graph: Graph) -> None:

      Recebe um grafo e, através do método pickNextCity, gera um ciclo, partindo de self.city. Quando finaliza um ciclo, registra suas informações em lastPath e lastPathDistance.

    
    def calcPheromoneToBeDeposited(self) -> float:

      Não recebe parâmetros. Através de self.lastPathDistance, retorna o feromônio a ser depositado nesse caminho. 
    
    def genPheromoneDepositMatrix(self, graph: Graph) -> Matrix:

      Recebe um grafo como parâmetro, usa calcPheromoneToBeDeposited para decidir quanto feromônio depositar e retorna uma matriz com os locais onde será deixado o feromônio. 
  
  ""Aco"" - aco.py

    Aco efetivamente une as entidades criadas e as utiliza na solução do problema. Possui as seguintes propriedades: 
      - graph (O grafo que representa o problema); 
      - ants (Uma lista de formigas);
      - decayRate (taxa de evaporação do feromônio)
      - iterations (número de iterações a serem feitas)
      - currentBestPath (melhor caminho)
      - currentBestPathDistance (distância do melhor caminho)
      - pheromoneInfluence (Influência do feromônio)
      - visibilityInfluence (Influência da visibilidade)
    
    Em seu construtor são recebidos os parâmetros necessários à construção do problema (caminho do arquivo, número de formigas, taxa de evaporação e número de iterações). Abaixo, seguem seus métodos:

    def decayPheromone(self):

      Aplica a evaporação do feromônio na matriz de feromônio (self.graph.scoreMatrix).
    
    def layNewPheromone(self):

      Para cada formiga em self.ants, é obtida sua matriz de depósito de feromônio, cujos valores são somados à matriz de feromônio (self.graph.scoreMatrix)
    
    def travelSingleAnt(self, ant: Ant) -> Ant:

      Recebe uma formiga e chama seu método travel. Ao final, retorna a formiga.

    def makeAntsTour(self, showTimes: bool = False) -> None:

      Recebe um parâmetro showTimes que apenas diz se a função deve mostrar seu tempo de execução. O método chama travelSingleAnt para cada formiga em self.ants. Ao final, executa as rotinas de evaporação e depósito de feromônio, bem como redistribui as formigas de maneira.  

    def getBestValues(self):

      Itera pelas formigas e obtém o melhor caminho feito entre elas. O caminho é atribuído a self.currentBestPath e sua distância, a self.currentBestPathDistance
    
    def startACO(self, showTimes: bool = False, showPartialResults: bool = False) -> None:

      Recebe um parâmetro showTimes e outro showPartialResults, que definem se os tempos de cada iteração de makeAntsTour serão mostrados, bem como seus resultados parciais.

      O método executa makeAntsTour() "self.iterations" vezes. Ao final, ele obtém os melhores valores gerados.
    

  ""main()"" - main.py

    O método main() cria uma instância de Aco com os valores definidos nas variáveis globais presentes no topo do arquivo. Após isso, ele chama o método startACO(). Findada a execução do programa são mostrados o melhor caminho encontrado, seu custo e o tempo de execução. Abaixo as variáveis globais mencionadas e seus valores padrão.

      FILENAME = "fri26_d.txt"
      ITERATIONS: int = 100
      ANT_NUMBER: int = 5
      DECAY_RATE: float = 0.5
      SHOW_EACH_ITERATION_TIME: bool = False
      PHEROMONE_INFLUENCE: float = 0.6
      VISIBILITY_INFLUENCE: float = 5


