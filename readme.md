# Mini-projeto Lista de Espera

#### **Integrantes:**    

​	**Heverton de Oliveira Lourenço** e 
​    **José Adrian Torres dos Santos**

#### Conteúdos de consulta:

​	**Adrian e Heverton:**

​		Material disponibilizado no classroom para desenvolver a base da fila (comum) e das listas encadeadas

***Conseguimos realizar tudo o que foi proposto.***

#### Dificuldades:

​	**Heverton:**

​		De inicio foi complicado entender como funcionava os ponteiros (self.proximo) e as funções da classe Noh. Manipular as variáveis para que elas apontassem corretamente para o próximo sem perder suas conexões dentro das funções de append(), pop() e inserir() deu trabalho, pois requer uma ordem lógica certa para que não se perca tais apontadores. O uso da variável self.tail é cruxial para o append ser O(1), e entender como fazer sua manipulação sem gerar erros requeriu algumas horas de neurônios fritando. Após entender o funcionamento dessas coisas o resto foi simples. Foi interessante também ver o funcionamento do método __str__ tanto no Noh quanto na ListaNaoOrdenada.

​	**Adrian:**

​		Achei esse projeto mais simples que o anterior, até por isso estou com umas dúvidas: Quanto a fila encadeada, qual nível de semelhança com a comum é exigido? Pois, utilizando lista encadeada, não a tornamos circular e nem definimos uma capacidade para ela, fazendo com que não seja necessário também a função de alterar tamanho; Outra dúvida é quanto a função "girar", eu consegui na fila circular, inicialmente, fazer essa função como O(1), pois eu apenas alterava a posição de inicio de acordo com a quantidade de vezes que iria girar e tirava a razão da capacidade da fila, tornando o inicio uma posição a mais e consequentemente o inicio anterior se tornando a última posição. Como essa fila encadeada não é circular, a função girar está como O(1), mas ela só faz um giro apenas, a quantidade de vezes que vai girar na fila é definido em um "for ", com base nas vezes que o usuário der como parâmetro na função menu, dentro do "Main" do projeto, ou seja, ela continua sendo O(1) mesmo com a quantidade de giros, ainda que não dentro da função, seja feito em um "for"?