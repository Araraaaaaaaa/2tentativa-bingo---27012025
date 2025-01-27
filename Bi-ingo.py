import random
permanencia = True
Joga1 = {(50,70,80,90),
         (51,72,82,91)}
Joga2 = {(53,65,83,92),
         (50,78,82,95)}
conjunto = {}
ganhadores = 0

def cartelas(J1, J2):
    #________________________________________________________Sorteio
    for Indic, List1 in enumerate(J1):
        for Indice, Number in enumerate(List1):
            if Indice == 0:
                J1[Indic][0] = random.randint(1,10)
                J2[Indic][0] = random.randint(1,10)
            elif Indice == 1:
                J1[Indic][1] = random.randint(11,20)
                J2[Indic][1] = random.randint(11,20)
            elif Indice == 2:
                J1[Indic][2] = random.randint(21,30)
                J2[Indic][2] = random.randint(21,30)
            elif Indice == 3:
                J1[Indic][3] = random.randint(31,40)
                J2[Indic][3] = random.randint(31,40)
    #_____________________________________________________________________________________Correção 
    for Indicelin, Linha in enumerate(J1):
        for Indi, Number in enumerate(Linha):
            if J1[0][Indi] == J1[1][Indi]: # verifica se tem algum igual
                if Indi == 0: # separa pelos parâmetros
                    if J1[0][Indi] < 9: #verifica se é um número difícil de alterar
                        J1[0][Indi] += 2
                    else:
                        J1[1][Indi] -= 2
                elif Indi == 1:
                    if J1[0][Indi] < 19: 
                        J1[0][Indi] += 2
                    else:
                        J1[1][Indi] -= 2
                elif Indi == 2:
                    if J1[0][Indi] < 29: 
                        J1[0][Indi] += 2
                    else:
                        J1[1][Indi] -= 2
                elif Indi == 3:
                    if J1[0][Indi] < 39: 
                        J1[0][Indi] += 2
                    else:
                        J1[1][Indi] -= 2
    for Indicelin, Linh in enumerate(J2):
        for Ind, Number in enumerate(Linh):
            if J2[0][Ind] == J2[1][Ind]: # verifica se tem algum igual
                if Ind == 0: # separa pelos parâmetros
                    if J2[0][Ind] < 9: #verifica se é um número difícil de alterar
                        J2[0][Ind] += 2
                    else:
                        J2[1][Ind] -= 2
                elif Indi == 1:
                    if J2[0][Ind] < 19: 
                        J2[0][Ind] += 2
                    else:
                        J2[1][Ind] -= 2
                elif Indi == 2:
                    if J2[0][Ind] < 29: 
                        J2[0][Ind] += 2
                    else:
                        J2[1][Ind] -= 2
                elif Indi == 3:
                    if J2[0][Ind] < 39: 
                        J2[0][Ind] += 2
                    else:
                        J2[1][Ind] -= 2
    return J1, J2 

def Jogin(Homem1, Homem2): 
    falta1 = 0
    falta2 = 0
    # _______________________________#
    print("         Jogador 1")
    print(f"{Homem1[0][0]}  {Homem1[0][1]}   {Homem1[0][2]}")
    print(f"{Homem1[1][0]}  {Homem1[1][1]}   {Homem1[1][2]}")
    print(f"{Homem1[2][0]}  {Homem1[2][1]}   {Homem1[2][2]}")
    print("         Jogador 2")
    print(f"{Homem2[0][0]}  {Homem2[0][1]}   {Homem2[0][2]}")
    print(f"{Homem2[1][0]}  {Homem2[1][1]}   {Homem2[1][2]}")
    print(f"{Homem2[2][0]}  {Homem2[2][1]}   {Homem2[2][2]}")
    # _______________________________#
    while ganhadores == 0:        
        sorteio = random.randint(1,30)#!
        for Indica,X in (conjunto):#_________________________________Corrige caso sorteie um número já sorteado
            while sorteio == X:
                sorteio = random.randint(1,30)#!
        conjunto.append(sorteio)

        # ______________________________________________________________________________Marca os sorteados
        for i,N1 in enumerate(Homem1):
            for v,NN1 in enumerate(N1):
                if sorteio == NN1:      #se algum número de Homem1 for sorteado
                    Homem1[i][v] = f"<{NN1}>"
                    falta1 += 1
        for i,N2 in enumerate(Homem2):
            for v,NN2 in enumerate(N2):
                if sorteio == NN1:      #se algum número de Homem1 for sorteado
                    Homem2[i][v] = f"<{NN2}>"
                    falta2 += 1

        print(f"Sorteio = {sorteio}", end='    ')
        print(f"Sorteados = {conjunto}")
        if len(conjunto) > 1 : #_________________________________________________________________________Ajeita a ordem da lista
            for endereco , ele in enumerate(conjunto):
                if conjunto[len(conjunto)-1] != conjunto[endereco]: #verifica se é o último elemento.
                    if conjunto[endereco] > conjunto[endereco + 1]:#se maior que seu sucessor: 
                        conjunto[endereco] = conjunto[endereco + 1] 
                        conjunto[endereco + 1] = ele
                else:
                    if conjunto[endereco] < conjunto[endereco - 1]:#se menor que seu antecessor: 
                        conjunto[endereco] = conjunto[endereco - 1] 
                        conjunto[endereco + 1] = ele
        
        print("         Jogador 1                                   Jogador 2")
        print(f"{Homem1[0][0]}  {Homem1[0][1]}   {Homem1[0][2]}                 {Homem2[0][0]}  {Homem2[0][1]}   {Homem2[0][2]}")
        print(f"{Homem1[1][0]}  {Homem1[1][1]}   {Homem1[1][2]}                 {Homem2[1][0]}  {Homem2[1][1]}   {Homem2[1][2]}")
        print(f"{Homem1[2][0]}  {Homem1[2][1]}   {Homem1[2][2]}                 {Homem2[2][0]}  {Homem2[2][1]}   {Homem2[2][2]}")
        



 
def Jogo(dificuldade, Homem1, Homem2):
    print("Hello Word")

# ______________________________________________________________________Código Principal

while permanencia == True:
    print("Qual o nível de dificuldade?")
    print("Rápido = 1   |   Longo  = 2")
    D = int(input())
    Impar, Par = cartelas(Joga1,Joga2)
    if D == 1:
        Jogin(Impar,Par)
    else:
        Jogo(Impar,Par)
