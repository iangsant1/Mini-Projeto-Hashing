# Mini-Projeto-Hashing

Registros de testes de tempo:
        Estes testes foram auxiliados pela IA. Tentei fazer primeiramente com 50000 linhas e 1000
    buscas, mas acabou não rodando do jeito que esperava. Provavelmente ficou pesado demais.
        Vale ressaltar também sobre os testes que há variações de tempo, mas é normal devido as
    variações do próprio sistema operacional, entre outros n motivos.

1º Teste:

RESULTADOS DE DESEMPENHO (5000 linhas, 100 buscas)
Tempo de Construção do Índice: 0.018836 s
Tempo Médio de Busca (Índice Invertido): 0.00011414 s
Tempo Médio de Busca (Varredura Completa): 0.03778489 s
O índice invertido foi 331.0x mais rápido por busca.

RESULTADOS DE DESEMPENHO (5000 linhas, 100 buscas)
Tempo de Construção do Índice: 0.025321 s
Tempo Médio de Busca (Índice Invertido): 0.00049327 s
Tempo Médio de Busca (Varredura Completa): 0.03977530 s
O índice invertido foi 80.6x mais rápido por busca.

RESULTADOS DE DESEMPENHO (5000 linhas, 100 buscas)
Tempo de Construção do Índice: 0.028874 s
Tempo Médio de Busca (Índice Invertido): 0.00034164 s
Tempo Médio de Busca (Varredura Completa): 0.03311876 s
O índice invertido foi 96.9x mais rápido por busca.

Em todas as vezes o índice invertido foi consideravelmente maior por busca.

2º teste:

O teste agora foi executado sem o processo de criação do índice, para vermos qual seria a diferença de desempenho. Sendo a mediana das 3 execuções: 

RESULTADOS DE DESEMPENHO (5000 linhas, 1 busca)
Tempo Médio de Busca (Índice Invertido): 0.00023000 s
Tempo Médio de Busca (Varredura Completa): 0.02918950 s 

RESULTADOS DE DESEMPENHO (5000 linhas, 10 busca)
Tempo Médio de Busca (Índice Invertido): 0.00022265 s
Tempo Médio de Busca (Varredura Completa): 0.02988493 s

RESULTADOS DE DESEMPENHO (5000 linhas, 100 busca)
Tempo Médio de Busca (Índice Invertido): 0.00021432 s
Tempo Médio de Busca (Varredura Completa): 0.03343713 s

RESULTADOS DE DESEMPENHO (5000 linhas, 1000 busca)
Tempo Médio de Busca (Índice Invertido): 0.00017567 s
Tempo Médio de Busca (Varredura Completa): 0.03518142 s

3º Teste:
Agora será executado o teste com o processo de criação de indice para o mesmo número de busca. Sendo utilizado a mediana das 3 execuções: 

RESULTADOS DE DESEMPENHO (5000 linhas, 1 busca)
Tempo de Construção do Índice: 0.016821 s
Tempo Médio de Busca (Índice Invertido): 0.00025070 s
Tempo Médio de Busca (Varredura Completa): 0.03698240 s
Tempo Construção do Índice + Índice Invertido: 0.01707140 s
Tempo Construção do Índice + Varredura Completa: 0.05380310 s

RESULTADOS DE DESEMPENHO (5000 linhas, 10 busca)
Tempo de Construção do Índice: 0.016719 s
Tempo Médio de Busca (Índice Invertido): 0.00014593 s
Tempo Médio de Busca (Varredura Completa): 0.03906191 s
Tempo Construção do Índice + Índice Invertido: 0.01686443 s
Tempo Construção do Índice + Varredura Completa: 0.05578041 s

RESULTADOS DE DESEMPENHO (5000 linhas, 100 busca)
Tempo de Construção do Índice: 0.014897 s
Tempo Médio de Busca (Índice Invertido): 0.00021245 s
Tempo Médio de Busca (Varredura Completa): 0.03862608 s
Tempo Construção do Índice + Índice Invertido: 0.01510935 s
Tempo Construção do Índice + Varredura Completa: 0.05352298 s


RESULTADOS DE DESEMPENHO (5000 linhas, 1000 busca)
Tempo de Construção do Índice: 0.016160 s
Tempo Médio de Busca (Índice Invertido): 0.00017888 s
Tempo Médio de Busca (Varredura Completa): 0.03962184 s
Tempo Construção do Índice + Índice Invertido: 0.01633908 s
Tempo Construção do Índice + Varredura Completa: 0.05578204 s

Conclusão

Nos testes feitos, nas condições que foram expostas, não houve um teste em que o índice invertido
foi menor, em questão de desempenho, do que a varredura completa. Mas isso aconteceu por conta da 
quantidade de linhas que foram colocadas para teste, porque o consumo de memória RAM é muito maior no 
indíce invertido. Possivelmente, em uma quantidade muito maior de texto, a varredura completa se pague. 
Porém, é previsto na literatura que o índice invertido será melhor que a varredura completa devido a 
notação big-O, em vista que a varredura completa trabalha em O(n) e o índice invertido trabalha em O(1).
A partir de 1 a 2 consultas a indexação já se paga, apesar desse tempo inicial ser cobrado, a velocidade 
e facilidade de busca em textos grandes logo se paga. O uso de set() ao invés de listas favorece a 
eliminação de duplicatas nas linhas, além de ter funções matemáticas prontas, como intersection() e 
issubset().
A construção do índice trabalha em O(N*M), tendo em vista que teremos N linhas e M o número médio de 
palavras por linha. Enquanto as operações de interseção e união trabalham em O(N), onde N é o número de 
elementos no conjunto. Enquanto a busca de valor em um dicionário trabalha em O(1), porque os dicionários
em python trabalham em tabelas hash, onde se calcula o hash e vai diretamente no endereço da memória
onde se está armazenado o conjunto de linhas.
Por fim, em relação a desvantagem da indexação se trata dos grandes textos, em que o consumo de memória
RAM é elevado. Também por isso tive que baixar a quantidade de linhas para o teste (notebook fraco não 
rodou), ao contrário da varredura completa em que utiliza consideravelmente menos memória RAM.


Sobre o uso de IA

A IA nesse projeto foi utilizada para a implementação de funções que desconhecia, como exemplo das 
funções de conjuntos como intersection(), até mesmo o uso do set() que ainda estava confuso em como ele
funcionaria como uma "Lista". Também foi utilizada para me guiar no teste de tempo, em como eu deveria 
executar e como registrar adequadamente o resultado. Tive problemas também de lógica para a escrita do
código inicialmente, fiz uma reestruturação do código inclusive porque estava confuso e não funcionava,
utilizei para guiar. Inicialmente não tive a ideia do for em chaves, salvo engano foi utilizada na
função de varredura completa em que usei buscar_e() e buscar_ou(), em que IA me ajudou a entender o 
porquê utilizar chaves ao invés de colchetes naquele caso.
Acabei de utilizar para verificar a estrutura dos códigos, e a IA percebeu que tinha um requisito pedido
que não tinha sido colocado, que era para retornar uma lista ordenada. Então atualizei com a função
sorted para retornar uma lista ordenada.