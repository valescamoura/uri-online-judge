# URI Online Judge | 1123 | Desvio de Rota

''' 
Descrição do problema:

O sistema rodoviário de um país interliga todas as suas N cidades de modo que, a partir de uma cidade qualquer, é possível chegar a cada uma das outras cidades trafegando pelas
estradas existentes. Cada estrada liga duas cidades distintas, tem mão dupla e um único posto de pedágio (o pedágio é pago nos dois sentidos de tráfego). As estradas não se 
intersectam a não ser nas cidades. Nenhum par de cidades é interligado por duas ou mais estradas.

A Transportadora Dias oferece um serviço de transporte de encomendas entre as cidades. Cada encomenda deve ser levada de uma cidade A para uma outra cidade B. A direção da 
Transportadora Dias define, para cada encomenda, uma rota de serviço, composta por C cidades e C−1 estradas: a primeira cidade da rota de serviço é a origem da encomenda, a 
última o destino da encomenda. A rota de serviço não passa duas vezes pela mesma cidade, e o veículo escolhido para fazer o transporte de uma encomenda pode trafegar apenas 
pela rota de serviço definida.

Certo dia, no entanto, o veículo que executava uma entrega quebrou e precisou ser levado para conserto em uma cidade que não está entre as cidades de sua rota de serviço. 
A direção da Transportadora Dias quer saber qual é o menor custo total, em termos de pedágio, para que o veículo entregue a encomenda na cidade destino, a partir da cidade 
em que foi consertado, mas com uma restrição adicional: se em algum momento o veículo passar por uma das cidades que compõem a sua rota de serviço, ele deve voltar a obedecer 
a rota de serviço.

Entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém quatro inteiros N, M, C e K (4 ≤ N ≤ 250, 3 ≤ M ≤ N×(N−1)/2, 2 ≤ C ≤ N−1 e C ≤ K ≤ N−1), 
representando, respectivamente, o número de cidades do país, o número de estradas, o número de cidades na rota de serviço e a cidade em que o veículo foi consertado. 
As cidades são identificadas por inteiros de 0 a N−1. A rota de serviço é 0, 1, ... , C−1, ou seja, a origem é 0, de 0 passa para 1, de 1 para 2 e assim por diante, até o 
destino C−1.

As M linhas seguintes descrevem o sistema rodoviário do país. Cada uma dessas linhas descreve uma estrada e contém três inteiros U, V e P (0 ≤ U, V ≤ N−1, U ≠ V, 0 ≤ P ≤ 250), 
indicando que há uma estrada interligando as cidades U e V com custo de pedágio P. O último caso de teste é seguido por uma linha contendo quatro zeros separados por espaço em 
branco.

Saída
Para cada caso de teste, o seu programa deve imprimir uma única linha, contendo um único inteiro T, o custo total mínimo necessário, em termos de pedágio, para que o veículo 
chegue ao destino.
'''

import heapq

# Input
n, m, c, k = list(map(int, input().split())) 

while n != 0 and m != 0 and c != 0 and k != 0:
    # definir listas de adjacências
    n_out = [[] * n for i in range(n)] 
    # definir a matriz de custos (pesos) 
    custo = []                          
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(0)
            else:
                linha.append(-1)
        custo.append(linha)

    infty = 1
    for j in range(m):    # ler as m arestas do grafo
        a, b, pedagio = list(map(int, input().split())) 
        n_out[a].append(b)             # b é vizinho de saída de a
        n_out[b].append(a)             # a é vizinho de saída de b
        custo[a][b] = pedagio
        custo[b][a] = pedagio
        infty = infty + pedagio     

    # Modificação da matriz de custos    
    for i in range(len(custo)):
            for j in range(len(custo[0])):
                # se existe um caminho:
                if custo[i][j] != -1:
                    # se os dois vértices estão na rota, mas não são consecutivos
                    # então o caminho não pode ser feito para se adequar a ordem do enunciado
                    if i < c and j < c and abs(i-j) != 1:
                        custo[i][j] = infty
                    # se um dos vértices está na rota e o outro não, então apenas o caminho no sentido 
                    # de fora para dentro da rota pode ser realizado, pois o caminhão não pode sair da rota 
                    if i >= c and j < c:
                        custo[j][i] = infty
                # se não existe caminho:
                elif custo[i][j] == -1:
                    custo[i][j] = infty
                # caso contrário, não fazer nada -> (se os vertices não estão na rota)
        
    # Inicializações
    marca = n*[0]
    L = n*[infty]
    L[k] = 0                                    # raiz k
    D = [(0, k)]                                # cada posição do heap guarda (L(w), w)
    for w in range(n):
        if w != k:
            heapq.heappush(D,(L[w],w))          # iniciar o heap com todos os valores

    while D != []:
        Lmin, v = heapq.heappop(D)              # tirar a raiz do heap
        marca[v] = 1
        for w in n_out[v]:
            if marca[w] == 0:
                if L[v] + custo[v][w] < L[w]:
                    pos = D.index((L[w],w))      # achar posicao de w no heap
                    L[w] = L[v] + custo[v][w]    # atualizar o valor de L[w]
                    D[pos] = (L[w],w)
                    heapq._siftdown(D,0,pos)     # atualizar o heap
                    
    print(L[c-1])

    n, m, c, k = list(map(int, input().split()))
