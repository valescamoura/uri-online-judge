'''
URI Online Judge | 1152 | Estradas Escuras
Univeristy of Ulm Local Contest - Alemanha
Timelimit: 3

https://www.urionlinejudge.com.br/judge/pt/problems/view/1152
'''

# Problema resolvido utilizando o algoritmo de Prim

import heapq

# Ler número de junções de Byteland (nós do grafo) e estradas (arestas)
n, m = input().split()
n = int(n)
m = int(m)

while n != 0 and m != 0:
    # Valor total gasto para iluminar todas as estradas
    valor_total = 0

    H = []
    n_out = [[] for i in range(n)]

    # Ler as m arestas do digrafo
    for j in range(m):  
        # Ler aresta de a para b com custo c              
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)   
        n_out[a].append((b, c))
        n_out[b].append((a, c))

        # Incrementar valor total de iluminação das estradas
        valor_total += c
  
    raiz = 0
    for (x, c) in n_out[raiz]:
        heapq.heappush(H, (c, raiz, x))

    n_edges = 0
    custo_tot = 0
    marcados = [False for i in range(n)]
    marcados[raiz] = True
    
    while n_edges < n-1:
        while True:
            (c, a, b) = heapq.heappop(H)
            if marcados[b] == False:
                break
        marcados[b] = True
        custo_tot += c
        
        n_edges += 1
        for (x,c) in n_out[b]:
            if marcados[x] == False:
                heapq.heappush(H, (c, b, x))

    # Valor a ser economizado pelo governo de Byteland é o valor total que seria gasto menos o custo mínimo
    print(valor_total-custo_tot)
    
    # Ler input novamente
    n, m = input().split()
    n = int(n)
    m = int(m)


'''
Exemplo de input
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
0 0
'''
