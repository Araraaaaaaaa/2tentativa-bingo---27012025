import random
permanencia = True
Joga1 = [[0,0,0,0],
         [0,0,0,0]]
Joga2 = [[0,0,0,0],
         [0,0,0,0]]
conjunto = []
ganhadores = 0
numerosinit = [ 1, 11, 21, 31]
numerosfini = [10, 20, 30, 40]

def cartelas(J1, J2):
    #________________________________________________________Sorteio
    for Indic, List1 in enumerate(J1):
        for Indice, Number in enumerate(List1):
            a = random.randint(numerosinit[Indice], numerosfini[Indice])
            b = random.randint(numerosinit[Indice], numerosfini[Indice])
            J1[Indic][Indice] = a
            J2[Indic][Indice] = b
    #_____________________________________________________________________________________Correção 
    for Linha in (J1):
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
    for Linh in (J2):
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
    fim = 0
    falta1 = 9
    falta2 = 9
    # _______________________________#
    print(" Jogador 1")
    print(f"{Homem1[0][0]}  {Homem1[0][1]}   {Homem1[0][2]}")
    print(f"{Homem1[1][0]}  {Homem1[1][1]}   {Homem1[1][2]}")
    print(" Jogador 2")
    print(f"{Homem2[0][0]}  {Homem2[0][1]}   {Homem2[0][2]}")
    print(f"{Homem2[1][0]}  {Homem2[1][1]}   {Homem2[1][2]}")
    # _______________________________#
    while fim == 0:
        fim = 0     
        sorteio = random.randint(1,30)#!
        # if len(conjunto) > 1 :
        #     for X in (conjunto):#_________________________________Corrige caso sorteie um número já sorteado
        #         if sorteio == X:
        #             sorteio = random.randint(1,30)#!
        conjunto.append(sorteio)

        # ______________________________________________________________________________Marca os sorteados
        for i,N1 in enumerate(Homem1):
            for v,NN1 in enumerate(N1):
                if sorteio == NN1:      #se algum número de Homem1 for sorteado
                    Homem1[i][v] = f"<{NN1}>"
                    falta1 -= 1
        for i,N2 in enumerate(Homem2):
            for v,NN2 in enumerate(N2):
                if sorteio == NN2:      #se algum número de Homem1 for sorteado
                    Homem2[i][v] = f"<{NN2}>"
                    falta2 -= 1

        set(conjunto) #_____________retira os números repetidos na lista
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
        
        print("Jogador 1                  Jogador 2")
        print(f"{Homem1[0][0]}  {Homem1[0][1]}   {Homem1[0][2]}                 {Homem2[0][0]}  {Homem2[0][1]}   {Homem2[0][2]}")
        print(f"{Homem1[1][0]}  {Homem1[1][1]}   {Homem1[1][2]}                 {Homem2[1][0]}  {Homem2[1][1]}   {Homem2[1][2]}")
    
        #_____________________________________________________Relação dos ganhadores
        if falta2 == 0 or falta1 == 0:
            fim = 5
            if falta1 == 0 and falta2 == 0:
                print("Bingo! Ambos jogadores ganharam \o/")
            elif falta1 == 0:
                print("Bingo! Jogador 1 ganhou \o/")
            else:
                print("Bingo! Jogador 2 ganhou \o/")
        input("Continue?")
        



 
def Jogo(dificuldade, Homem1, Homem2):
    print("Hello Word")

# ______________________________________________________________________Código Principal

while permanencia == True:
    print("Rápido = 1   |   Longo  = 2")
    print("Qual o nível de dificuldade?", end=" ")
    D = int(input())

    Impar, Par = cartelas(Joga1,Joga2)
    if D == 1:
        Jogin(Impar,Par)
    else:
        Jogo(Impar,Par)
