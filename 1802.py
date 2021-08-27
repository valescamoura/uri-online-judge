'''
URI Online Judge | 1802 | Catálogo de Livros
Por Thalyson Nepomuceno, Universidade Estadual do Ceará BR Brazil
Timelimit: 2

Bino está elaborando um catálogo de livros escolares. Ele está organizando um catálogo com conjuntos distintos de livros para vender em sua loja online. Cada conjunto de livros 
é formado por 5 livros, sendo um de cada matéria (português, matemática, física, química e biologia). Dois conjuntos de livros são considerados distintos se existe pelo menos 
um livro que está em um e não está no outro. Bino quer expor no site apenas os conjuntos distintos mais caros, e pediu sua ajuda.

O valor de um conjunto é a soma dos valores de cada livro que está nele. Sua tarefa é informar qual a soma dos valores dos K conjuntos distintos de livros mais caros. 
Em caso de empate entre conjuntos mais caros, Bino escolhe qualquer um dos conjuntos empatados.

Entrada
A entrada consiste em 6 linhas: A primeira linha contém um inteiro P (5 ≤ P ≤ 10), representando que Bino tem P tipos diferentes de livros de português, seguido por P inteiros
vi ( 1 ≤ vi ≤ 1000), representando os valores de cada livro de português.  A segunda linha contém um inteiro M (5 ≤ M ≤ 10), representando que Bino tem M tipos diferentes de 
livros de matemática, seguido por M inteiros vi ( 1 ≤ vi ≤ 1000), representando os valores de cada livro de matemática. A terceira linha contém um inteiro F (5 ≤ F ≤ 10), 
representando que Bino tem F tipos diferentes de livros de física, seguido por F inteiros vi ( 1 ≤ vi ≤ 1000), representando os valores de cada livro de física. A quarta linha 
contém um inteiro Q (5 ≤ Q ≤ 10), representando que Bino tem Q tipos diferentes de livros de química, seguido por Q inteiros vi ( 1 ≤ vi ≤ 1000), representando os valores de 
cada livro de química. A quinta linha contém um inteiro B (5 ≤ B ≤ 10), representando que Bino tem B tipos diferentes de livros de biologia, 
seguido por B inteiros vi ( 1 ≤ vi ≤ 1000), representando os valores de cada livro de biologia. A sexta linha contém um inteiro K (1 ≤ K ≤ P*M*Q*F*B), representando a
quantidade de conjuntos distintos de livros que o catálago de livros terá.

Saída
Imprima o valor da soma dos valores dos K conjuntos distintos de livros mais caros.
'''

portugues = list(map(int,input().split()))
matematica = list(map(int,input().split()))
fisica = list(map(int,input().split()))
quimica = list(map(int,input().split()))
biologia = list(map(int,input().split()))

k = int(input())

conjuntos = []

for p in range(1, portugues[0]+1):
    for m in range(1, matematica[0]+1):
        for f in range(1, fisica[0]+1):
            for q in range(1, quimica[0]+1):
                for b in range(1, biologia[0]+1):
                    soma = portugues[p]+ matematica[m] + fisica[f] + quimica[q] + biologia[b]
                    conjuntos.append(soma)
                
conjuntos.sort(reverse=True)

soma = 0
for i in range(k):
    soma += conjuntos[i]

print(soma)
