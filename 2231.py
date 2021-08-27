'''
URI Online Judge | 2231 | Temperatura Lunar
Por OBI - Olimpíada Brasileira de Informática 2002 BR Brazil
Timelimit: 1

Sem as proteções da atmosfera e do cinturão magnético que existem na Terra, a Lua fica exposta ao ataque do Sol, que é um astro em constante explosão atômica. As explosões do 
Sol emitem ondas letais de partículas. Uma pessoa que ficasse desprotegida na superfície da Lua, num lugar onde o Sol incidisse diretamente, sofreria um bombardeio radioativo 
tão intenso quanto se estivesse nas imediações da usina russa de Chernobyl no momento do acidente que matou 31 pessoas, em 1986. Além da radiação solar, outro efeito desta 
falta de proteção contra o Sol que existe na Lua é a enorme variação de temperatura. Nas regiões próximas do equador lunar, a variação de temperatura é brutal, passando de 
cerca de 130 graus positivos durante o dia a 129 graus negativos à noite.

Para estudar com mais precisão as variações de temperatura na superfície da Lua, a NASA enviou à Lua uma sonda com um sensor que mede a temperatura de 1 em 1 minuto. Um dado 
importante que os pesquisadores desejam descobrir é como se comporta a média da temperatura, considerada em intervalos de uma dada duração (uma hora, meia hora, oito horas, etc.). 
Por exemplo, para a seqüência de medições 8, 20, 30, 50, 40, 20, -10, e intervalos de quatro minutos, as médias são respectivamente 108/4=27, 140/4=35, 140/4=35 e 100/4=25.

Você foi recentemente contratado pela NASA, e sua primeira tarefa é escrever um programa que, conhecidos a seqüência de temperaturas medidas pelo sensor, e o tamanho do
intervalo desejado, informe qual a maior e qual a menor temperatura média observadas, considerando o tamanho do intervalo dado. 

Entrada
A entrada é composta de vários conjuntos de teste. A primeira linha de um conjunto de teste contém dois números inteiros positivos N (0 ≤ N ≤ 10000) e M (1 ≤ M ≤ N), que 
indicam respectivamente o número total de medições de temperatura (-200 ≤ temperatura ≤ 200) de uma seqüência obtida pelo sensor, e o tamanho dos intervalos, em minutos, em 
que as médias devem ser calculadas. As N linhas seguintes contêm um número inteiro cada, representando a seqüência de medidas do sensor. O final da entrada é indicado quando 
N = M = 0.

Saída
Para cada conjunto de teste da entrada seu programa deve produzir três linhas. A primeira linha identifica o conjunto de teste, no formato “Teste n”, onde n é numerado a 
partir de 1. A segunda linha deve conter dois números inteiros X e Y, separados por ao menos um espaço em branco, representando respectivamente os valores da menor e da maior 
média de temperatura, conforme determinado pelo seu programa. O valor da média deve ser truncado, se a média não for um número inteiro (ou seja, deve ser impressa apenas a 
parte inteira). A terceira linha deve ser deixada em branco. A grafia mostrada no Exemplo de Saída, abaixo, deve ser seguida rigorosamente.
'''

from math import trunc
teste = 1
linha = list(map(int, input().split()))
n = linha[0]
m = linha[1]

while n!=0 and m!=0:
    
    temp = []
    tempAcumulada = [0] * (n+1)

    for i in range(n):
        x = int(input())
        temp.append(x)
        
    for i in range(n):
        a = tempAcumulada[i]
        b = temp[i]
        tempAcumulada[i+1] = a + b

    maximo = -9999999
    minimo = 9999999
    v = 0
    u = m
    while u <= n:
        soma = tempAcumulada[u] - tempAcumulada[v]
        if soma>maximo:
            maximo = soma
        if soma<minimo:
            minimo = soma
            
        v+=1
        u+=1
    
    maximo = trunc(maximo/m)
    minimo = trunc(minimo/m)
    print("Teste {}".format(teste))
    print(minimo, maximo)
    print()
    teste+=1
    linha = list(map(int, input().split()))
    n = linha[0]
    m = linha[1]
