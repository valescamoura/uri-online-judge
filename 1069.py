'''
URI Online Judge | 1069 | Diamantes e Areia
Por Neilor Tonin, URI  Brasil
Timelimit: 1

João está trabalhando em uma mina, tentando retirar o máximo que consegue de diamantes "<>". Ele deve excluir todas as particulas de areia "." do processo e a cada retirada 
de diamante, novos diamantes poderão se formar. Se ele tem como uma entrada .<...<<..>>....>....>>>., três diamantes são formados. O primeiro é retirado de <..>, 
resultando  .<...<>....>....>>>. Em seguida o segundo diamante é retirado, restando .<.......>....>>>. O terceiro diamante é então retirado, restando no final .....>>>., 
sem possibilidade de extração de novo diamante.

Entrada
Deve ser lido um valor inteiro N que representa a quantidade de casos de teste. Cada linha a seguir é um caso de teste que contém até 1000 caracteres, incluindo "<,>, ."

Saída
Você deve imprimir a quantidade de diamantes possíveis de serem extraídos em cada caso de entrada.
'''

n = input()
for i in range(int(n)):
    string = input()
    diamantes = 0
    abre = 0
    for i in range(len(string)):
        if string[i] == "<":
            abre += 1
        elif string[i] == ">" and abre > 0:
            diamantes += 1
            abre -= 1
            
    print(diamantes)
