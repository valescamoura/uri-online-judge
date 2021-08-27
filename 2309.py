'''
URI Online Judge | 2309 | Truco

Truco é um jogo de cartas que pode ser jogado por duas ou mais pessoas. Existem diversas variações: o Truco Cego ou Truco Espanhol (popular no sul do Brasil, Argentina, Uruguai 
e outros países), o Truco Paulista, Capixaba ou Mineiro (variações populares no Brasil), o Truco Índio e o Truco Eteviano. Em geral, é uma disputa de três rodadas (“melhor de três”)
para ver quem tem as cartas mais “fortes” (de valor simbólico mais alto).

Adalberto e Bernardete estão jogando uma variação de truco com 40 cartas (foram retirados do baralho todas as cartas de valor 8, 9 e 10, além dos coringas), e o valor simbólico 
independente do naipe da carta. A ordem de valor simbólico das cartas nessa variação de truco é mostrada abaixo, ordenada da mais “fraca” (mais à esquerda) para a mais “forte” 
(mais à direita)

4 5 6 7 Q J K A 2 3

Cada partida é disputada em três rodadas. A cada rodada, os jogadores escolhem uma das cartas para mostrar, e vence aquele que tiver a carta com o maior valor simbólico. 
Em caso de empate (ou seja, os dois apresentarem cartas com os mesmos valores simbólicos), Adalberto vence, pois é mais velho que Bernardete. Vence a partida aquele que vencer 
o maior número de rodadas.

Depois de algumas partidas, Adalberto e Bernardete estão com dificuldades para saber quem venceu mais partidas, e pediram a sua ajuda.

Sua tarefa é escrever um programa que calcule o número de partidas que cada um dos competidores (Adalberto e Bernardete) venceram.

Entrada
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A primeira linha da saída possui um inteiro N que indica
o número de partidas disputadas entre Adalberto e Bernardete (1 ≤ N ≤ 1000000). As N linhas seguintes contêm cada uma seis inteiros, A1, A2, A3, B1, B2 e B3 , que correspondem 
às três cartas apresentadas por Adalberto nas rodadas 1, 2 e 3 daquela partida (A1, A2, A3 ∈ {1, 2, 3, 4, 5, 6, 7, 11, 12, 13}), seguidas pelas três cartas apresentadas por 
Bernardete nas rodadas 1, 2 e 3 da mesma partida (B1, B2, B3 ∈ {1, 2, 3, 4, 5, 6, 7, 11, 12, 13}). Na entrada, o número 1 representa o Ás  (A), 11 representa o Valete (J), 12 
representa a Dama (Q) e 13 representa o Rei (K).

Saída
Seu programa deve imprimir, na saída padrão, uma única linha, que contém os números de partidas vencidas por Adalberto e por Bernadete, nessa ordem, separados por espaços.
'''

n = int(input())
a = 0
b = 0
contA = 0
contB = 0

for _ in range(n):

    cartas = input().split()

    for x in range(6):

        if cartas[x] == '11':
            cartas[x] = 13
        elif cartas[x] == '13':
            cartas[x] = 14
        elif cartas[x] == '1':
            cartas[x] = 15
        elif cartas[x] == '2':
            cartas[x] = 16
        elif cartas[x] == '3':
            cartas[x] = 17
            
    for i in range(3):

        if int(cartas[i]) >= int(cartas[i+3]):
            contA += 1
        else:
            contB += 1

    if contA > contB:
        a += 1
    else:
        b += 1

    contA = 0
    contB = 0

print(a, b)
