'''
URI Online Judge | 2303 | Margaridas
Por OBI - Olimpíada Brasileira de Informática 2006 BR Brazil
Timelimit: 1

Leopoldo é gerente de uma plantação de flores da Associação de Cultivo de Margaridas (ACM), um grupo que cultiva margaridas em grandes propriedades para abastecer floriculturas
em grandes cidades.

As margaridas são plantadas em vasos dispostos em linhas e colunas, formando uma espécie de grade. Na plantação administrada por Leopoldo existem L linhas de vasos de margaridas,
cada uma formada por C vasos. Para facilitar o gerenciamento, os vasos são organizados em lotes de M linhas e N colunas de vasos, sendo que não existem sobreposições entre os 
lotes (não existe nenhuma linha ou coluna comum a mais de um lote) e todos os lotes têm exatamente M linhas e N colunas.

A colheita é sempre feita em um único lote, coletando-se todas as margaridas daquele lote que estejam prontas para a venda. Uma semana antes de fazer a colheita, os 
funcionários da plantação analisaram cada vaso e anotaram quantas margaridas estarão prontas para venda na semana seguinte. Leopoldo agora precisa da sua ajuda para determinar 
qual o número máximo de margaridas que poderá ser colhido em um único lote de M × N vasos.

Sua tarefa é escrever um programa que, dado um mapa da plantação contendo o número de margaridas prontas para venda em cada vaso, encontre qual o número máximo de margaridas 
que podem ser colhidos por Leopoldo.

Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A primeira linha da entrada contém quatro números 
inteiros, L, C, M e N. L e C representam respectivamente o número de linhas (1 ≤ L ≤ 1000) e de colunas (1 ≤ C ≤ 1000) de vasos existentes na plantação. M e N representam 
respectivamente o número de linhas (1 ≤ M ≤ L) e de colunas (1 ≤ N ≤ C) dos lotes. As L linhas seguintes contêm C inteiros cada, representando número de margaridas prontas 
para colheita no vaso localizado naquela linha e coluna. Note que L M e C N são sempre inteiros, pois não há linha ou coluna de vasos que pertença a mais de um lote.

Saída
Seu programa deve imprimir, na saída padrão, uma única linha que contém o número máximo de margaridas que podem ser colhidos em um lote de M × N. Esse número não pode ser 
superior a 1000000.
'''

linha = list(map(int, input().split()))
l = linha[0]
c = linha[1]
m = linha[2]
n = linha[3]

matriz = []

for i in range(l):
    matriz.append(list(map(int, input().split())))

#print(matriz)

maximo = -1

x = 0
a = m
while a<=l:
    y = 0
    b = n
    while b<=c:
        soma = 0
        for i in range(x,a):
            for j in range(y,b):
                soma += matriz[i][j]
        #print(soma)
        if soma>maximo:
            maximo = soma
        y+=n
        b+=n 
    x+=m
    a+=m
    
print(maximo)
